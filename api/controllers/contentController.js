const contentModel = require("../models/contentModel");

// a function to get the questions from the mongo database
exports.getQuestions = async (req, res, next) => {
  try {
    const questions = await contentModel.find();
    res.status(200).json(questions);
  } catch (err) {
    if (!err.statusCode) {
      err.statusCode = 500;
    }
    next(err);
  }
};
