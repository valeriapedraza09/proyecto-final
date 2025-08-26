CREATE DATABASE PROYECTO_1103;
USE PROYECTO_1103;
CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Ingredientes (
    id_ingrediente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ingrediente VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Recetas (
    id_receta INT PRIMARY KEY AUTO_INCREMENT,
    nombre_receta VARCHAR(255) NOT NULL,
    id_categoria INT,
    tiempo_preparacion_min INT,
    dificultad VARCHAR(50),
    instrucciones TEXT,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

CREATE TABLE Recetas_Ingredientes (
    id_receta INT,
    id_ingrediente INT,
    PRIMARY KEY (id_receta, id_ingrediente),
    FOREIGN KEY (id_receta) REFERENCES Recetas(id_receta) ON DELETE CASCADE,
    FOREIGN KEY (id_ingrediente) REFERENCES Ingredientes(id_ingrediente) ON DELETE CASCADE
);