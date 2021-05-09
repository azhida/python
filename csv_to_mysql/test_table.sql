/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : 127.0.0.1:3306
 Source Schema         : test_db

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 09/05/2021 13:29:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test_table
-- ----------------------------
DROP TABLE IF EXISTS `test_table`;
CREATE TABLE `test_table`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `created_at` datetime(0) NULL DEFAULT NULL,
  `updated_at` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test_table
-- ----------------------------
INSERT INTO `test_table` VALUES (17, 'name_1', ' ', '2021-05-09 12:37:54', '2021-05-09 12:37:57');
INSERT INTO `test_table` VALUES (18, 'name_2', NULL, '2021-05-09 12:38:11', NULL);
INSERT INTO `test_table` VALUES (19, 'name_3', '备注', NULL, '2021-05-09 12:38:28');
INSERT INTO `test_table` VALUES (20, 'name_4', NULL, NULL, NULL);
INSERT INTO `test_table` VALUES (21, 'name_5', '0', '2021-05-09 12:38:50', '2021-05-09 12:38:53');

SET FOREIGN_KEY_CHECKS = 1;
