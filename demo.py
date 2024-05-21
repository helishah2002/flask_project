# from flask import Flask
# import logging

# def create_app():
#     app = Flask(__name__)
    
#     # Configure logging
#     logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
#     # @app.route('/')
#     # def index():
#     #     app.logger.info('Accessed index route')
#     #     return 'Hello, World!'

#     # return app
    


# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     try:
#         # Code that may raise exceptions
#         raise Exception('Something went wrong')
#     except Exception as e:
#         app.logger.error('An error occurred: %s', e)
#         return 'An error occurred', 500