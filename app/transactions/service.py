from app.transactions.repository import TransactionRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    # GET TRANSACTIONS PAGINATE
    def get_transactions_paginate(self, skip: int, limit: int):
        transactions = self.transaction_repository.get_paginated(skip, limit)
        
        # We need total count for pagination metadata
        total_transactions = self.transaction_repository.count()
        
        # Avoid division by zero
        total_pages = total_transactions // limit if limit > 0 else 0
        current_page = len(transactions) # This logic looks weird in original too (current_page = len(transactions)?).
        # Original: current_page = len(transactions). If page size is 10, current_page is 10?
        # Usually current_page means page index.
        # But let's keep original logic to strictly refactor structure not logic, unless logic is broken.
        # Original: current_page = len(transactions)
        
        message = {
            "total_pages": total_pages,
            "current_page": current_page,
            "total_transactions": total_transactions,
        }

        return {"transactions": transactions, "message": message}
