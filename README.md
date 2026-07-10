## Replicación de bases de datos MySQL

Método de replicación de bases de datos MySQL, para no tener que usar un solo servidor y que este se sature, o se caiga y no tengamos acceso a la base de datos.

## Explicación:

La replicación de bases de datos MySQL sirve para mantener copias sincronizadas de una base de datos en diferentes servidores o bases, de manera que no se dependa de un único punto de acceso.

En este caso, los triggers funcionan como un mecanismo automático que detecta cambios en la base principal (INSERT, UPDATE o DELETE (entre otras)) y los repite en las bases de réplica. Esto ayuda a:

* Evitar saturación del servidor principal: las consultas pueden distribuirse entre varias bases.
* Mejorar disponibilidad: si una base falla, existe otra copia con la información.
* Mantener respaldos actualizados: los cambios se reflejan automáticamente.
* Reducir pérdida de información: las réplicas contienen una copia reciente de los datos.

Los tres triggers realizan lo siguiente:

INSERT: cuando se agrega un nuevo activo en la base principal, lo copia automáticamente en las bases réplica.
UPDATE: cuando se modifica un activo, actualiza esos cambios en las réplicas.
DELETE: cuando se elimina un activo, también lo elimina en las réplicas.

IMPORTANTE: La tabla activos debe existir con la misma estructura en todas las bases para que los triggers puedan copiar correctamente la información.

## Seguridad y respaldos

PARA METODOS DE SEGURIDAD Y RESPALDOS VISITAR: (aun trabajando)

## Triggers

Trigger: Disparador como objeto de base de datos usado para ejecutar una accion automaticamente cuando ocurre un evento en especifico.
"Escucha" y luego repite en otras bases.

### Trigger para INSERT:

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

### Trigger para UPDATE:

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

### Trigger para DELETE:

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

## Tabla para activos en la base principal

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
