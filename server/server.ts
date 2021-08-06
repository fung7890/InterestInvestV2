import express from "express";
import dotenv from "dotenv";
import mongoose from "mongoose";
import { model, Schema, Model, Document } from "mongoose";
import { resolve } from "path";

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

dotenv.config({ path: resolve(__dirname, "../.env") });

const uri = `mongodb+srv://Admin:${process.env.DB_KEY}@cluster0.0qvxa.mongodb.net/${process.env.DB_NAME}?retryWrites=true&w=majority`;

const connectionParams = {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
};

mongoose
  .connect(uri, connectionParams)
  .then(() => {
    console.log("Connected to database ");
  })
  .catch((err) => {
    console.error(`Error connecting to the database. \n${err}`);
  });

const AccoutsSchema = new Schema({
  account_id: Number,
  limit: Number,
  products: [String],
});

const Account = model("Account", AccoutsSchema);

app.get("/", async (req, res) => {
  const result = await Account.find();
  res.send(JSON.stringify(result));
});

app.listen(3000, () => console.log("Server has started"));
