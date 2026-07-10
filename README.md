Metodo de replicación de bases de datos MySQL, para no tener que usar un solo servidor y que este se sature, o se caiga y no tengamos acceso a la base de datos.

Trigger: Disparador como objeto de base de datos usado para ejecutar una accion automaticamente cuando ocurre un evento en especifico.
"Escucha" y luego repite en otras bases.

Trigger para INSERT:

´´´bash
DELIMITER $$

CREATE TRIGGER tg_replica_activos_insert
AFTER INSERT ON repo_database.activos
FOR EACH ROW
BEGIN
    INSERT INTO repo_databasel.activos (id, placa, numero_serie, activo, ip, sede, area)
    VALUES (NEW.id, NEW.placa, NEW.numero_serie, NEW.activo, NEW.ip, NEW.sede, NEW.area);

    INSERT INTO repo_databases.activos (id, placa, numero_serie, activo, ip, sede, area)
    VALUES (NEW.id, NEW.placa, NEW.numero_serie, NEW.activo, NEW.ip, NEW.sede, NEW.area);
END$$

DELIMITER ;
´´´

Trigger para UPDATE:

´´´bash
DELIMITER $$

CREATE TRIGGER tg_replica_activos_update
AFTER UPDATE ON repo_database.activos
FOR EACH ROW
BEGIN
    UPDATE repo_databasel.activos
    SET placa = NEW.placa,
        numero_serie = NEW.numero_serie,
        activo = NEW.activo,
        ip = NEW.ip,
        sede = NEW.sede,
        area = NEW.area
    WHERE id = OLD.id;

    UPDATE repo_databases.activos
    SET placa = NEW.placa,
        numero_serie = NEW.numero_serie,
        activo = NEW.activo,
        ip = NEW.ip,
        sede = NEW.sede,
        area = NEW.area
    WHERE id = OLD.id;
END$$

DELIMITER ;
´´´

Trigger para DELETE:

´´´bash
DELIMITER $$

CREATE TRIGGER tg_replica_activos_delete
AFTER DELETE ON repo_database.activos
FOR EACH ROW
BEGIN
    DELETE FROM repo_databasel.activos WHERE id = OLD.id;
    DELETE FROM repo_databases.activos WHERE id = OLD.id;
END$$

DELIMITER ;
´´´

Tabla para activos en la base principal:
Esquema para crear las mismas tablas en las bases de replica, para que los triggers funcionen correctamente.
Deben coincidir todas.

´´´sql
CREATE TABLE IF NOT EXISTS activos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(50) NOT NULL,
    numero_serie VARCHAR(100),
    activo VARCHAR(20),
    ip VARCHAR(45),
    sede VARCHAR(100),
    area VARCHAR(100)
);
´´´
Insert de ejemplo para probar la replicación:

´´´sql
INSERT INTO activos (placa, numero_serie, activo, ip, sede, area)
VALUES 
('422723', 'SN123456789', 'Laptop', '192.168.1.105', 'Sede Central', 'Oficina TI');
´´´

