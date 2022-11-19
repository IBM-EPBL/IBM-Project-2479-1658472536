from flask import Flask, render_template, request
import pickle
model = pickle.load(open('university.pkl','rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        gre = request.form['gre']
        toefl = request.form['toefl']
        universityNumber = request.form['universityNumber']
        sop = request.form['sop']
        lor = request.form['lor']
        cgpa = request.form['cgpa']
        research = request.form['research']

        y_pred = [[gre, toefl, universityNumber, sop, lor, cgpa, research]]
        print(y_pred)
        prediction_value = model.predict(y_pred)
        print(prediction_value)
        if prediction_value == 'Yes':
            return render_template('chance.html')
        if prediction_value == 'No':
            return render_template('Nochance.html')
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)