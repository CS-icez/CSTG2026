CREATE TRIGGER trig_reply_ai AFTER INSERT ON reply
FOR EACH ROW
BEGIN
    UPDATE post
    SET reply_cnt = reply_cnt + 1
    WHERE post_id = NEW.post_id;
END;
