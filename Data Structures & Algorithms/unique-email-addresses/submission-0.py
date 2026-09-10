class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_dict = {}
        for s in emails:
            local, domain = s.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            formatted = local + '@' + domain
            email_dict[formatted] = True
        return len(email_dict)
        