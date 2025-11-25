require('dotenv').config()
const Pool = require('pg').Pool
const pool = new Pool({
    user: process.env.PG_USER,
    host: 'localhost',
    database: 'node_test',
    password: process.env.PG_PASSWORD,
    port: 5432,
})

const createProduct = (req, res) => {
    const {product_name, product_quantity} = req.body

    pool.query('INSERT INTO products (p_name, p_quantity) VALUES ($1, $2)', 
        [product_name, product_quantity], (err, results) => {
            if(err){
                throw err
            }
            res.status(201).send(`Product added with ID: ${results.insertId}`)
        })
}

const getProducts = (req, res) => {
  pool.query('SELECT * FROM products ORDER BY id ASC', (err, results) => {
    if (err) {
      throw err
    }
    res.status(200).json(results.rows)
  })
}


module.exports = {
    createProduct,
    getProducts,
}