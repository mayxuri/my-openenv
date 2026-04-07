"""
Synthetic customer support ticket dataset.
Each ticket includes the ground-truth answer used by the grader.
"""

TASK1_TICKETS = [
    {
        "ticket_id": "T001",
        "subject": "Can't login to my account",
        "body": (
            "I've been trying to login for the past hour but keep getting 'Invalid credentials'. "
            "I'm sure my password is correct because I just changed it yesterday. "
            "Please help me regain access to my account as soon as possible!"
        ),
        "customer_name": "Alice Johnson",
        "account_type": "pro",
        "created_at": "2024-01-15T10:30:00Z",
        "previous_tickets": [],
        "answer": {"category": "account"},
    },
    {
        "ticket_id": "T002",
        "subject": "Charged twice for my subscription",
        "body": (
            "I noticed two charges of $49.99 on my credit card statement dated January 10th. "
            "I only have one subscription under this account. "
            "Please refund the duplicate charge immediately."
        ),
        "customer_name": "Bob Martinez",
        "account_type": "pro",
        "created_at": "2024-01-15T11:00:00Z",
        "previous_tickets": [],
        "answer": {"category": "billing"},
    },
    {
        "ticket_id": "T003",
        "subject": "API returning 500 Internal Server Error",
        "body": (
            "Since this morning, all our API calls to /api/v2/users are returning "
            "500 Internal Server Error. This is breaking our production application. "
            "Error: InternalServerError: null pointer exception at line 342. "
            "Please investigate urgently."
        ),
        "customer_name": "Carol Chen",
        "account_type": "enterprise",
        "created_at": "2024-01-15T09:15:00Z",
        "previous_tickets": [],
        "answer": {"category": "technical"},
    },
    {
        "ticket_id": "T004",
        "subject": "How do I export my project data?",
        "body": (
            "I want to export all my project data to CSV format for analysis. "
            "I've looked through the settings and help docs but can't find the export option. "
            "Could you guide me on how to do this? Thanks!"
        ),
        "customer_name": "David Kim",
        "account_type": "free",
        "created_at": "2024-01-15T14:30:00Z",
        "previous_tickets": [],
        "answer": {"category": "general"},
    },
    {
        "ticket_id": "T005",
        "subject": "Invoice not received after plan upgrade",
        "body": (
            "I upgraded my plan from Pro to Enterprise last week but haven't received "
            "the invoice yet. I need it for my company's expense report by end of month. "
            "My account email is eva@techcorp.com."
        ),
        "customer_name": "Eva Wilson",
        "account_type": "enterprise",
        "created_at": "2024-01-15T16:00:00Z",
        "previous_tickets": [],
        "answer": {"category": "billing"},
    },
    {
        "ticket_id": "T006",
        "subject": "Two-factor authentication code always expired",
        "body": (
            "The 2FA code I receive via SMS is always expired by the time I enter it. "
            "I've checked and my phone's time is synced correctly. "
            "This has effectively locked me out of my account for two days."
        ),
        "customer_name": "Frank Brown",
        "account_type": "pro",
        "created_at": "2024-01-15T13:45:00Z",
        "previous_tickets": [],
        "answer": {"category": "account"},
    },
    {
        "ticket_id": "T007",
        "subject": "Dashboard loading extremely slowly",
        "body": (
            "The dashboard has been extremely slow to load for the past 3 days. "
            "It takes over 30 seconds to display the main page. "
            "My internet is fine — other websites load normally. Please investigate."
        ),
        "customer_name": "Grace Lee",
        "account_type": "pro",
        "created_at": "2024-01-15T10:00:00Z",
        "previous_tickets": [],
        "answer": {"category": "technical"},
    },
    {
        "ticket_id": "T008",
        "subject": "Difference between Pro and Enterprise plans?",
        "body": (
            "I'm currently on the Pro plan with a team of 50 people. "
            "I'm wondering whether upgrading to Enterprise would be beneficial. "
            "Can you explain the main differences and whether it's worth upgrading for our use case?"
        ),
        "customer_name": "Henry Zhang",
        "account_type": "pro",
        "created_at": "2024-01-15T11:30:00Z",
        "previous_tickets": [],
        "answer": {"category": "general"},
    },
]

TASK2_TICKETS = [
    {
        "ticket_id": "T101",
        "subject": "URGENT: Production system completely down",
        "body": (
            "Our entire production environment is down. ALL API calls return 500 errors. "
            "10,000 active users are affected and we are losing approximately $50k per hour. "
            "This started 15 minutes ago with no recent deployments on our end. "
            "CRITICAL EMERGENCY — please respond immediately."
        ),
        "customer_name": "Bob Smith",
        "account_type": "enterprise",
        "created_at": "2024-01-15T14:00:00Z",
        "previous_tickets": [
            {"ticket_id": "T099", "subject": "API latency spike", "resolved": True}
        ],
        "answer": {
            "category": "technical",
            "priority": "critical",
            "team": "technical_team",
        },
    },
    {
        "ticket_id": "T102",
        "subject": "Is dark mode available on mobile?",
        "body": (
            "Hi! I was just wondering whether the dark mode feature is available on the mobile app. "
            "I use it frequently and would love to have dark mode to reduce eye strain. Thanks!"
        ),
        "customer_name": "Sarah Lee",
        "account_type": "free",
        "created_at": "2024-01-15T10:00:00Z",
        "previous_tickets": [],
        "answer": {
            "category": "general",
            "priority": "low",
            "team": "customer_success",
        },
    },
    {
        "ticket_id": "T103",
        "subject": "Refund request — charged after cancellation",
        "body": (
            "I cancelled my Pro subscription 3 days ago but was still charged $99 for the next month. "
            "I have cancellation confirmation #CANCEL-2024-789. "
            "Please process a full refund to my original payment method."
        ),
        "customer_name": "Michael Johnson",
        "account_type": "free",
        "created_at": "2024-01-15T09:30:00Z",
        "previous_tickets": [],
        "answer": {
            "category": "billing",
            "priority": "high",
            "team": "billing_team",
        },
    },
    {
        "ticket_id": "T104",
        "subject": "Cannot change account email address",
        "body": (
            "I'm trying to update my account email from old@company.com to new@company.com "
            "but keep getting 'Email already in use' error even though that email has no account. "
            "This is blocking a staff transition for our 200-person organisation."
        ),
        "customer_name": "Emma Davis",
        "account_type": "enterprise",
        "created_at": "2024-01-15T11:00:00Z",
        "previous_tickets": [],
        "answer": {
            "category": "account",
            "priority": "medium",
            "team": "account_team",
        },
    },
    {
        "ticket_id": "T105",
        "subject": "Webhooks not firing for payment events",
        "body": (
            "Our payment webhook endpoint has not received any events for the past 6 hours. "
            "We rely on this for real-time payment processing in production. "
            "Our server logs show zero incoming requests from your service. "
            "Webhook URL: https://api.ourcompany.com/webhooks/payment"
        ),
        "customer_name": "James Wilson",
        "account_type": "enterprise",
        "created_at": "2024-01-15T08:00:00Z",
        "previous_tickets": [
            {"ticket_id": "T098", "subject": "Webhook setup help", "resolved": True}
        ],
        "answer": {
            "category": "technical",
            "priority": "high",
            "team": "technical_team",
        },
    },
    {
        "ticket_id": "T106",
        "subject": "Invoice shows wrong amount",
        "body": (
            "The invoice for January shows $199/month but I'm on the $99/month Pro plan. "
            "This appears to be a billing error. Please correct the invoice and issue a revised one."
        ),
        "customer_name": "Lisa Thompson",
        "account_type": "pro",
        "created_at": "2024-01-15T15:00:00Z",
        "previous_tickets": [],
        "answer": {
            "category": "billing",
            "priority": "medium",
            "team": "billing_team",
        },
    },
]

TASK3_TICKETS = [
    {
        "ticket_id": "T201",
        "subject": "Refund request — duplicate charge",
        "body": (
            "I was charged $99 twice on January 10th for my Pro subscription. "
            "I only have one account. Please refund the duplicate charge. "
            "My account email is carol@startup.com."
        ),
        "customer_name": "Carol Davis",
        "account_type": "pro",
        "created_at": "2024-01-15T09:00:00Z",
        "previous_tickets": [],
        "answer": {
            "must_include_words": ["carol", "refund", "apologize"],
            "issue_keywords": ["duplicate", "charge"],
            "resolution_phrases": ["process", "business days", "team", "investigate", "confirm"],
            "min_words": 60,
            "max_words": 500,
        },
    },
    {
        "ticket_id": "T202",
        "subject": "URGENT: Cannot access data — production demo in 2 hours",
        "body": (
            "We cannot access any of our data. All API calls return 403 Forbidden since this morning. "
            "We have a demo with a major client in 2 hours. Our API key is still active. "
            "Please HELP URGENTLY."
        ),
        "customer_name": "David Park",
        "account_type": "enterprise",
        "created_at": "2024-01-15T08:30:00Z",
        "previous_tickets": [],
        "answer": {
            "must_include_words": ["david", "apologize"],
            "issue_keywords": ["403", "access"],
            "resolution_phrases": ["escalate", "investigate", "team", "immediately", "priority"],
            "min_words": 80,
            "max_words": 500,
        },
    },
    {
        "ticket_id": "T203",
        "subject": "How to set up SSO with Okta for our team?",
        "body": (
            "We are an enterprise customer and want to set up Single Sign-On (SSO) for our 200-person team. "
            "We use Okta as our identity provider. "
            "Can you walk us through the setup process?"
        ),
        "customer_name": "Emma Rodriguez",
        "account_type": "enterprise",
        "created_at": "2024-01-15T14:00:00Z",
        "previous_tickets": [],
        "answer": {
            "must_include_words": ["emma", "sso"],
            "issue_keywords": ["okta", "sso", "single sign"],
            "resolution_phrases": ["steps", "settings", "configuration", "guide", "documentation", "support"],
            "min_words": 80,
            "max_words": 600,
        },
    },
    {
        "ticket_id": "T204",
        "subject": "Password reset email never arrives",
        "body": (
            "I requested a password reset three times today but never received the email. "
            "I've checked spam/junk folders. My email is frank@example.com. "
            "I'm completely locked out of my account."
        ),
        "customer_name": "Frank Adams",
        "account_type": "free",
        "created_at": "2024-01-15T12:00:00Z",
        "previous_tickets": [],
        "answer": {
            "must_include_words": ["frank", "apologize"],
            "issue_keywords": ["password", "email", "reset"],
            "resolution_phrases": ["team", "investigate", "manually", "send", "alternative"],
            "min_words": 60,
            "max_words": 400,
        },
    },
]


def get_ticket_for_task(task_name: str, seed: int = 42) -> dict:
    """Return a single deterministic ticket for a task based on seed."""
    if task_name == "classify":
        pool = TASK1_TICKETS
    elif task_name == "route":
        pool = TASK2_TICKETS
    elif task_name == "respond":
        pool = TASK3_TICKETS
    else:
        raise ValueError(f"Unknown task: {task_name}. Choose: classify | route | respond")
    return pool[seed % len(pool)]
