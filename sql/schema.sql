-- sql/schema.sql

CREATE TABLE IF NOT EXISTS customers (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(200) NOT NULL,
    email      VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS products (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(200) NOT NULL,
    price NUMERIC      NOT NULL,
    stock INT          NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id          SERIAL PRIMARY KEY,
    customer_id INT          NOT NULL,
    product_id  INT          NOT NULL,
    quantity    INT          NOT NULL CHECK (quantity > 0),
    total       NUMERIC      NOT NULL,
    status      VARCHAR(20)  NOT NULL DEFAULT 'pendente',
    order_date  DATE         NOT NULL,

    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(id),
    CONSTRAINT fk_product  FOREIGN KEY (product_id)  REFERENCES products(id)
);