let conn;

$(function () {
    const mysql = require('mysql');
    conn = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'mysql231128',
        database: 'cstg',
    })
    conn.connection()
    let sql = 'show databases;'
    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err);
            return;
        }
        console.log(result);
    })
})