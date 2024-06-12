from src import create_app
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
