import os
import mysql.connector


def init_drupal():
    drupal_client = None
    try:
        drupal_client = mysql.connector.connect(
            host=os.environ.get('DR_DATABASE_HOST'),
            user=os.environ.get('DR_DATABASE_USER'),
            password=os.environ.get('DR_DATABASE_PASSWORD'),
            database=os.environ.get('DR_DATABASE_NAME'),
        )
        print('Drupal DB: OK')
    except Exception as e:
        print('Drupal DB: ' + str(e))


    return drupal_client
