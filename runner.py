import businesshandler as b

pas = "RandomPassword"
handle = b.BusinessHandler(pkey=pas)
handle.reset_db()
p_backup = "RandomPasswords.csv"
handle.extract_backup(backup_path=p_backup)
