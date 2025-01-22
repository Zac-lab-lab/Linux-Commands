from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Programming Exercise</title>
    </head>
    <body>
        <h1>Zac Hilton, SN: 9788967</h1>
        <p><font size="5"><font color="orange">World</font> <font color="blue">Gurning</font> <font color="purple">Competition</font> 😊</font></p>
        <table border="1">
            <tr>
                <td><b>Ranking</b></td>
                <td><b>Team</b></td>
                <td><b>Member</b></td>
            </tr>
            <tr>
                <td>Row 1</td>
                <td>
                    <div style="text-align: center;">
                        <a href="http://didd.gov" target="_blank">HackTheBox Website</a>
                        <br>
                        <img src="https://avatars.githubusercontent.com/u/31746234?s=280&v=4" width="300" alt="HackTheBox Logo">
                    </div>
                </td>
                <td>
                    <ul>
                        <li> <b>Zac</b> (<i>team captain</i>)</li>
                        <li>Bob (developer)</li>
                        <li>Alice (pentester)</li>
                        <li>Charlie (analyst)</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>Row 2</td>
                <td>
                    <div style="text-align: center;">
                        <a href="http://binn.gov" target="_blank">TryHackMe Website</a>
                        <br>
                        <img src="https://tryhackme-images.s3.amazonaws.com/user-avatars/83d369e0ec4156eef0b33faeed69346d.png" width="300" alt="TryHackMe Logo">
                    </div>
                </td>
                <td>
                    <ul>
                        <li> <b>Stuart</b> (<i>team captain</i>)</li>
                        <li>Lucian (developer)</li>
                        <li>Trinity (pentester)</li>
                        <li>Ellen (analyst)</li>
                    </ul>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)