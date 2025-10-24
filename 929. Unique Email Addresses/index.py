from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_emails.add(local + '@' + domain)

        return len(unique_emails)


if __name__ == "__main__":
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]

    solution = Solution()
    result = solution.numUniqueEmails(emails)
    print("Number of unique emails:", result)
