# The Python code is based on Simon Wells' example Slightly More Complex Quiz from the Projectbook - Thank you!
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'SUPERSEKRETKEY'

@app.route("/")
def hello():
    session['question'] = 1
    session['question1'] = 1
    return render_template('index.html')

@app.route("/f1quiz/")
def f1quiz():
    q = None
    qa = {
        "1":{
            "text":"Who won the 2019 F1 Championship?",
            "answer":1,
            "answers":["Lewis Hamilton", "Max Verstappen", "Keke Rosberg", "Alexander Albon"]
        },
        "2":{
            "text":"Who won the 2020 F1 Championship?",
            "answer":1,
            "answers":["Lewis Hamilton", "Max Verstappen", "Keke Rosberg", "Alexander Albon"]
        },
        "3":{
            "text":"Who won the 2021 F1 Championship?",
            "answer":1,
            "answers":["Max Verstappen", "Lewis Hamilton", "Keke Rosberg", "Alexander Albon"]
        },
        "4":{
            "text":"Who won the 2022 F1 Championship?",
            "answer":1,
            "answers":["Max Verstappen", "Lewis Hamilton", "Keke Rosberg", "Alexander Albon"]
        },
        "5":{
            "text":"Who won the 2023 F1 Championship?",
            "answer":1,
            "answers":["Max Verstappen", "Lewis Hamilton", "Keke Rosberg", "Alexander Albon"]
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1
        
    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q+1
            session['question'] = q
            if q > len(qa):
                return render_template('success.html')
            else:
                return render_template('f1quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)
        else:
            return render_template('wrong.html', text="Wrong answer!")
    else:
        return render_template('f1quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q)

@app.route("/motoGPquiz/")
def motoGPquiz():
    y = None
    ya = {
        "1":{
            "text1":"Who won the 2019 MotoGP Championship?",
            "answer1":1,
            "answers":["Marc Marquez", "Jorge Martin", "Fabio Quartararo", "Joan Mir"]
        },
        "2":{
            "text1":"Who won the 2020 MotoGP Championship?",
            "answer1":1,
            "answers":["Joan Mir", "Jorge Martin", "Fabio Quartararo", "Marc Marquez"]
        },
        "3":{
            "text1":"Who won the 2021 MotoGP Championship?",
            "answer1":1,
            "answers":["Fabio Quartararo", "Jorge Martin", "Francesco Bagnaia", "Joan Mir"]
        },
        "4":{
            "text1":"Who won the 2022 MotoGP Championship?",
            "answer1":1,
            "answers":["Francesco Bagnaia", "Jorge Martin", "Fabio Quartararo", "Joan Mir"]
        },
        "5":{
            "text1":"Who won the 2023 MotoGP Championship?",
            "answer1":1,
            "answers":["Francesco Bagnaia", "Jorge Martin", "Fabio Quartararo", "Joan Mir"]
        }
    }
    try:
        if (session['question1']):
            y = int(session['question1'])
    except KeyError:
        y = 1
        
    answer1 = request.args.get('answer1', None)
    if answer1 is not None:
        correct = ya.get(str(y)).get('answer1')
        if str(answer1) == str(correct):
            y = y+1
            session['question1'] = y
            if y > len(ya):
                return render_template('success.html')
            else:
                return render_template('motoGPquiz.html', text1=ya[str(y)]["text1"], answers=ya[str(y)]["answers"], number1=y)
        else:
            return render_template('wrong.html', text1="Wrong answer!")
    else:
        return render_template('motoGPquiz.html', text1=ya[str(y)]["text1"], answers=ya[str(y)]["answers"], number1=y)
    
@app.route("/success/")
def success():  
    return render_template('success.html')

@app.route("/aboutUs/")
def aboutUs():   
    return render_template('aboutUs.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")