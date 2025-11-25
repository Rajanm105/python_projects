require('dotenv').config()
const express = require('express')
const db = require('./products')
const auth = require("./middlewares/auth")

const app = express()

app.use(express.json())
app.use(express.urlencoded({extended: true}))

app.get('/', (req, res) => {
    res.send("Product service is running")
})

app.get('/products',auth, db.getProducts)
app.post('/products/create/',auth, db.createProduct)

app.listen(process.env.PORT || 5000, () => {
    console.log(`Server started on port, ${process.env.PORT}`)
})