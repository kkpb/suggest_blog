from flask import Flask, render_template, request
from werkzeug import ImmutableDict
from sklearn.externals import joblib
import text_listing as tl
import os
import datetime
import json

class FlaskWithHamlish(Flask) :
    jinja_options = ImmutableDict(extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_', 'hamlish_jinja.HamlishExtension'])

app = FlaskWithHamlish(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/<mode>", methods=['GET', 'POST'])
def index(mode=None) :
    if request.method == 'POST' :
        print request.form.getlist('useful')
        param = zip(request.form.getlist('text'), request.form.getlist('useful'))
        data = []
        for text, useful in param :
            data.append({'entry':text, 'useful':useful})
        with open('train/'+str(datetime.datetime.today())+".json", 'w') as f :
            json.dump(data, f, indent=4)

    vectorizer = joblib.load('tmp_v/vec.pkl')
    print len(vectorizer.get_feature_names())
    clf = joblib.load('tmp_c/clf.pkl')
    data = 'json/'+os.listdir("json")[-1]
    data_text = tl.text_list_from_json(data, 'entry')
    data_v = vectorizer.transform(data_text)
    data_url = tl.text_list_from_json(data, 'url')
    data_title = tl.text_list_from_json(data, 'title')
    result = zip(data_title, data_url, clf.predict(data_v.todense()), data_text)
    print clf.predict(data_v.todense())
    headline = "All Blog"
    if mode == 'useful' :
        headline = "Interesting"
        result = filter(lambda (_,__,n,___) : n == 1, result)
    elif mode == 'useless' :
        headline = "NotInteresting"
        result = filter(lambda (_,__,n,___) : n == 0, result)

    return render_template('index.haml', headline = headline, result = result)
    
if __name__ == "__main__" :
    app.run(debug=True)
