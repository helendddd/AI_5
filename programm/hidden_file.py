#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск скрытых файлов.
# Найти все скрытые файлы (файлы, начинающиеся с точки . ) в файловом дереве.
# Начинать с глубины 20 уровней и продвигаться до глубины 15 уровней.
# Для каждой итерации увеличивается глубина поиска на 10 уровней.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"


class Problem:
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal


def depth_limited_search(problem, limit):
    frontier = [(problem.root, 0)]  # Добавляем кортеж (узел, текущая глубина)
    while frontier:
        node, depth = frontier.pop()
        # Проверка на цель
        if problem.goal(node.value):
            return node
        if depth < limit:  # Если текущая глубина меньше лимита
            for child in node.children:
                frontier.append((child, depth + 1))
    return None


def find_hidden_files(problem):
    hidden_files = []
    limit = 20
    # Выполнение поиска на разных глубинах
    while limit >= 5:  # Уменьшаем глубину до минимальной (например, до 5)
        result = depth_limited_search(problem, limit)
        if result:
            hidden_files.append(result.value)
        limit -= 5  # Уменьшаем глубину на 5
    return hidden_files


if __name__ == "__main__":
    # Создаем файловую структуру
    root = TreeNode("root")
    dir1 = TreeNode("dir1")
    dir2 = TreeNode("dir2")
    hidden_file = TreeNode(".hidden_file")
    regular_file = TreeNode("file1")
    dir1.add_child(hidden_file)
    dir1.add_child(regular_file)
    root.add_children(dir1, dir2)

    # Устанавливаем цель поиска
    def goal(value):
        return value.startswith(".")  # Проверка на скрытые файлы

    # Запуск задачи
    problem = Problem(root, goal)
    hidden_files = find_hidden_files(problem)

    if hidden_files:
        print("Найденные скрытые файлы:", hidden_files)
    else:
        print("Скрытые файлы не найдены.")
