CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carat` INTEGER NOT NULL,
    `price` NUMERIC(5,2)
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NAVCHAR(160) NOT NULL,
    `Price` NUMERIC(5,2)
);

INSERT INTO `Metals` VALUES (null, "gold", 40.50);
INSERT INTO `Metals` VALUES (null, "silver", 36.80);
INSERT INTO `Metals` VALUES (null, "iron", 19.75);

INSERT INTO `Orders` VALUES (null, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 1, 2, 3);
INSERT INTO `Orders` VALUES (null, 2, 3, 1);
INSERT INTO `Orders` VALUES (null, 3, 1, 2);

INSERT INTO `Sizes` VALUES (null, 20, 240.60);
INSERT INTO `Sizes` VALUES (null, 30, 765.12);
INSERT INTO `Sizes` VALUES (null, 15, 98.58);

INSERT INTO `Styles` VALUES (null, "trilliant", 60.60);
INSERT INTO `Styles` VALUES (null, "emerald", 74.56);
INSERT INTO `Styles` VALUES (null, "pear", 82.23);

