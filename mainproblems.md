Possível migração para SQLalchemy quando possível.

Tirar a ordenação de TaskManager e mover para Storage com parametros no SQLite.

Desse jeito:

conditions = []
params = []

if nome is not None:
    conditions.append("name = ?")
    params.append(nome)

if done is not None:
    conditions.append("status = ?")
    params.append(done)

sql = "SELECT * FROM tasks"

if conditions:
    sql += " WHERE " + " AND ".join(conditions)

cursor.execute(sql, params)




Talvez padronizar a verificação futuramente com uma função.
