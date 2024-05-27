# CSTG 2026 Conference Website

Welcome to the repository for the CSTG2026 conference website. This website has been developed to provide information and updates about the upcoming CSTG2026 academic conference. Below you will find instructions on how to set up, configure, and contribute to this project.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Common Issues](#common-issues)
- [Pending Tasks](#pending-tasks)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

## Project Overview

The CSTG2026 conference website is a **fictional** project created for educational purposes. It is designed to demonstrate web development skills and does **not** represent a real conference.

## Features

- Comprehensive homepage
- Account management system
- Complete submission and review process
- User dashboard
- Integrated discussion forum
- Waiting for you to explore

## Installation

### Option 1: Docker (recommended)

Make sure Docker is available on your machine.

Pull image from Docker Hub:

```shell
docker pull icez26/cstg2026:latest
```

Start server:

```shell
docker run --rm -p 5000:5000 -it icez26/cstg2026
```

Now you can view our website at `http://localhost:5000`.

### Option 2: Local

Initialization:

1. Make sure that you have [Python](https://www.python.org/) and [MySQL](https://www.mysql.com) locally. We are running under Python 3.10.12 and MySQL 8.2.0. We do not guarantee that the project will run in other environments.
2. Install Python package Flask and Flask-Uploads.
3. Clone this repo.
4. Replace the user name and password in `db.py` with your MySQL account. Replace the `FLASK_APP` in `init_server.sh` and `start_server.sh` with the path of this repo.
5. Change to the parent directory of this repo and run `CSTG2026/init_server.sh`.

Start the deployment server: change to the parent directory of this repo and run `CSTG2026/start_server.sh`.

Now you can view our website at `http://localhost:5000`.

## Usage

Our website comes with some pre-initialized accounts for demonstration purposes. You can use these accounts to explore the features of our website. Alternatively, you can sign up a new account and then sign in.

| Email                  | Password | Role     |
| ---------------------- | -------- | -------- |
| stq0102@gmail.com      | 123456   | Author   |
| zissu@gmail.com        | 234567   | Author   |
| hao@gmail.com          | 345678   | Author   |
| clodhac@gmail.com      | 345678   | Author   |
| waithw@gmail.com       | 567890   | Author   |
| bowen111@gmail.com     | 678901   | Author   |
| slow0323@gmail.com     | 789012   | Author   |
| xianglady@gmail.com    | 890123   | Author   |
| confident@gmail.com    | 901234   | Author   |
| kai001@gmail.com       | 1234567  | Reviewer |
| ltr@gmail.com          | 2345678  | Reviewer |
| lpx@gmail.com          | 3456789  | Reviewer |
| huorwu@gmail.com       | 4567890  | Reviewer |
| teacher@gmail.com      | 5678901  | Reviewer |
| greenswallow@gmail.com | 6789012  | Reviewer |
| pirving@gmail.com      | 7890123  | Reviewer |
| cheat@gmail.com        | 8901234  | Reviewer |

## Common Issues

During installation, you may encounter some common issues. Here are solutions to help you resolve them.

If your encounter an error like

```
Error: While importing 'CSTG2026', an ImportError was raised:

Traceback (most recent call last):
  File "/home/icez/.local/lib/python3.10/site-packages/flask/cli.py", line 247, in locate_app
    __import__(module_name)
  File "/home/icez/college/CSTG2026/__init__.py", line 2, in <module>
    from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
  File "/home/icez/.local/lib/python3.10/site-packages/flask_uploads.py", line 26, in <module>
    from werkzeug import secure_filename, FileStorage
ImportError: cannot import name 'secure_filename' from 'werkzeug' (/home/icez/.local/lib/python3.10/site-packages/werkzeug/__init__.py)
```

when running `init_server.sh`. Execute

```shell
sed -i 's/from werkzeug import secure_filename, FileStorage/from werkzeug.utils import secure_filename\nfrom werkzeug.datastructures import FileStorage/' /home/icez/.local/lib/python3.10/site-packages/flask_uploads.py
```

and rerun `init_server.sh`. Remember to replace the path of `flask_uploads.py` with your own.

## Pending Tasks

There are several features and improvements that are still in progress or planned for future development:

1. **Edit Account Information:** Now you cannot modify your personal information after registering an account, which is clearly unreasonable.
2. **Enhanced Forum Features:** We plan to add features such as sorting, filtering, and searching forum content, as well as the ability to like, bookmark, and share posts and replies.
3. **Messaging System:** We plan to implement a messaging system that notifies users when their submissions are reviewed or when their posts receive replies.
4. **Mobile Optimization:** Many pages currently do not display correctly on small devices. We are short-staffed, but we are working on it.

Contributions to any of these tasks are welcome!

## Contributing

We welcome contributions from the community! To contribute, please follow these steps:

1. Fork this repo

2. Create a new branch

   ```shell
   git checkout -b feature/your-feature-name
   ```

3. Make your changes

4. Commit your changes

   ```shell
   git commit -m "Add your commit message"
   ```

5. Push to the branch

   ```shell
   git push origin feature/your-feature-name
   ```

6. Create a pull request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## Disclaimer

This website is a course project and is entirely fictional. Any resemblance to real conferences, events, or organizations is purely coincidental. All information, including user profiles, emails, and papers, is created for educational purposes and does not reflect any real-world entities or events.

## Contact

For any inquiries or further information, please contact the project maintainer at cstg2026@gmail.com. (Do not contact. This is also fictional.)
