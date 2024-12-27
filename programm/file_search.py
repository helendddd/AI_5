#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

    def is_goal(self, node):
        return node.value == self.goal

    def expand(self, node):
        return node.children


def depth_limited_search(node, problem, limit):
    if problem.is_goal(node):
        return [node.value]
    if limit == 0:
        return "cutoff"

    for child in problem.expand(node):
        path = depth_limited_search(child, problem, limit - 1)
        if path != "cutoff":
            return [node.value] + path
    return "cutoff"


def iterative_deepening_search(problem):
    depth = 0
    while True:
        result = depth_limited_search(problem.root, problem, depth)
        if result != "cutoff":
            return result
        depth += 1


if __name__ == "__main__":
    # Построение дерева
    root = TreeNode("dir")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file4"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))

    # Создание задачи
    goal = "dir2"
    problem = Problem(root, goal)

    # Поиск пути
    path = iterative_deepening_search(problem)
    print(" -> ".join(path))
