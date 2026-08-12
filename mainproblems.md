None for now.

Open opencode sessions when possible.

Snippet
        tasks = self._storage.read()
        for task in tasks:
            print(f"[{'✓' if task.done else '-'}] {task.id}: {task.nome}")
