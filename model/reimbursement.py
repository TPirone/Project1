class Reimbursement:
    def __init__(self, id, amount, submitted, resolved, status, reimb_type_id, description, receipt, user_id, resolver_id):
        self.id = id
        self.amount = amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.reimb_type_id = reimb_type_id
        self.description = description
        self.receipt = receipt
        self.usr_id = user_id
        self.resolver_id = resolver_id

    def to_dict(self):
        return {
            
        }