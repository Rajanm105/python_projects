module.exports = function (req, res, next) {
  const userId = req.headers["x-user-id"];
  const username = req.headers["x-user-name"];

  if (!userId || !username) {
    return res.status(401).json({ error: "Unauthorized access — headers missing" });
  }

  req.user = { id: userId, username: username };
  next();
};