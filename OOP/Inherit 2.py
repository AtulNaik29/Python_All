class OttSubscription:
    def __init__(self,subscription_id,plan,payment):
        self.id=subscription_id
        self.plan=plan
        self.payment=payment

    def subscribe(self):
        print(f'Subscribe with {self.id}id subscribed to the {self.plan}plan')

    def unsubscribe(self):
        print(f'Subscribe with {self.id}id unsubscribed to the {self.plan}plan')


netflix=OttSubscription(11221,"monthly",100)
netflix.plan