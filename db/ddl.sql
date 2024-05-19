use cstg;

CREATE TABLE usr (
    usr_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender ENUM('M', 'F') NOT NULL,
    email VARCHAR(50) NOT NULL,
    passwd VARCHAR(50) NOT NULL,
    type ENUM('A', 'R')
);

CREATE TABLE paper (
    paper_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    abstract TEXT NOT NULL,
    status ENUM('P', 'A', 'R') NOT NULL,
    reviewer_id INT NOT NULL,
    FOREIGN KEY (reviewer_id) REFERENCES usr(usr_id)
);

CREATE TABLE publishes (
    usr_id INT NOT NULL,
    paper_id INT NOT NULL,
    PRIMARY KEY (usr_id, paper_id),
    FOREIGN KEY (usr_id) REFERENCES usr(usr_id),
    FOREIGN KEY (paper_id) REFERENCES paper(paper_id)
);

CREATE TABLE section (
    sec_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL
);

CREATE TABLE post (
    post_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    sec_id INT NOT NULL,
    pub_id INT NOT NULL,
    pub_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sec_id) REFERENCES section(sec_id),
    FOREIGN KEY (pub_id) REFERENCES usr(usr_id)
);

CREATE TABLE reply (
    reply_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    content TEXT NOT NULL,
    post_id INT NOT NULL,
    pub_id INT NOT NULL,
    pub_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (pub_id) REFERENCES usr(usr_id)
);
