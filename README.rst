Manage Boards and Ideas
=================
Create an api rest that allows us to manage the transaction creation on boards and ideas in a web application

Api Root
========
* **URL**: ``/api/``

* **METHOD**: ``GET``

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

       {
            "users": "http://localhost:8000/api/users/",
            "boards": "http://localhost:8000/api/boards/",
            "ideas": "http://localhost:8000/api/ideas/",
        }

Obtain Auth Token
=================

* **URL**: ``/api-token-auth/``

* **METHOD**: ``POST``

* **DATA PARAMS**: ``{"username": admin, "password": "********" }``

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

    {"token": "xxxxxxx-12345-aaaa-bbbb-9876-xxxx"}


List User
============

* **URL**: ``/api/auth/users/``

* **METHOD**: ``GET``

* **Header** *(Authorization)* : *Token* ``xxxxxxx-12345-aaaa-bbbb-9876-xxxx``

.. code-block:: json

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

       {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
            {
                "id": 1,
                "username": "admin",
                "password": "pbkdf2_sha256$120000$ozvNOpp13k0R$Uu7Q2dYUHos487OMrRGXCNZGSVRpEvdGqUBVdnTVZYo=",
                "first_name": "",
                "last_name": "",
                "identificacion": "333"
        ]
       }


List Boards
============

* **URL**: ``/api/auth/boards/``

* **METHOD**: ``GET``

* **Header** *(Authorization)* : *Token* ``xxxxxxx-12345-aaaa-bbbb-9876-xxxx``

* **URL Params Filter**: ``estado``

.. code-block:: json

        ?estado=PUBLICO

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

       {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 195,
                    "nombre": "Hacer curso de Android",
                    "estado": "PRIVADO",
                    "board": 7
                },
                {
                    "id": 196,
                    "nombre": "Ir a cine",
                    "estado": "PRIVADO",
                    "board": 7
                }
            ]
       }



Create Board
=============

* **URL**: ``/api/boards/``

* **METHOD**: ``POST``

* **Header** *(Authorization)* : *Token* ``xxxxxxx-12345-aaaa-bbbb-9876-xxxx``

* **Data Params:**:

.. code-block:: json

    {"nombre": "Nuevo Tablero", "estado": "PRIVADO"}


* **Estado**:
    * *PRIVADO*
    * *PUBLICO*

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

    {
        "id": 1,
        "nombre": "Nuevo Tablero",
        "estado": "PRIVADO",
        "board": 7
    }


List Ideas
============

* **URL**: ``/api/auth/ideas/``

* **METHOD**: ``GET``

* **Header** *(Authorization)* : *Token* ``xxxxxxx-12345-aaaa-bbbb-9876-xxxx``

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

       {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 84,
                    "nombre": "Nueva tarea",
                    "estado": "PRIVADO",
                    "board": 32
                },
                {
                    "id": 194,
                    "nombre": "Entrevista de trabajo",
                    "estado": "PRIVADO",
                    "board": 33
                }
            ]
       }

Create Idea
=============

* **URL**: ``/api/ideas/``

* **METHOD**: ``POST``

* **Header** *(Authorization)* : *Token* ``xxxxxxx-12345-aaaa-bbbb-9876-xxxx``

* **Data Params:**:

.. code-block:: json

    {"nombre": "Nueva Idea", "estado": "PRIVADO"}


* **Estado**:
    * *PRIVADO*
    * *PUBLICO*

* **Success Response**:
    * **Code**: ``200 OK``
    * **Content**:

.. code-block:: json

    {
        "id": 194,
        "nombre": "Entrevista de trabajo",
        "estado": "PRIVADO",
        "board": 33
    }

Colaboradores
=================

@chingal
