from flaskr import create_app
import logging.config
import logging
import os

app = create_app()

if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__name__))
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    if os.getenv('ENVIRONMENT', 'development') == 'development':
        log_file_path = os.path.join(basedir, 'flaskr', 'config', 'development', 'logger.conf')
        debug_mode = True
    else:
        log_file_path = os.path.join(basedir, 'flaskr', 'config', 'production', 'logger.conf')
        debug_mode = False
    logging.config.fileConfig(fname=log_file_path) 
    from flask.logging import default_handler
    app.logger.removeHandler(default_handler)
    app.run(debug=debug_mode)
