#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit):
    # Если достигли максимальной глубины, возвращаем False
    if limit < 0:
        return False
    # Если текущий узел является целевым, возвращаем True
    if node is None:
        return False
    if node.value == goal:
        return True
    # Ищем в левом и правом поддереве, уменьшая лимит глубины
    return depth_limited_search(
        node.left, goal, limit - 1
    ) or depth_limited_search(node.right, goal, limit - 1)


def iterative_deepening_search(root, goal):
    limit = 0
    while True:
        # Запуск поиска с ограничением глубины
        if depth_limited_search(root, goal, limit):
            return True
        limit += 1


def main():
    # Построение дерева
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    # Целевое значение
    goal = 4

    # Выполнение итеративного углубления
    result = iterative_deepening_search(root, goal)
    print(result)  # Ожидаемый вывод: True


if __name__ == "__main__":
    main()
