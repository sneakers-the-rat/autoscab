import argparse
import pprint
import sys
from autoscab.deployments import Deployment
from autoscab.constants import colors

parser = argparse.ArgumentParser("autoscab", epilog="IF THEY WANT SCABS, WE'LL GIVE EM SCABS")

parser.add_argument('deployment', help="Which deployment to run", default='', nargs='?')
parser.add_argument('--email', help="Which method of email generation to use",
                    default="random", choices=['random', 'guerillamail', 'mailtm'])
parser.add_argument('-n', type=int, default=1, help="Apply for n jobs (default: 1)")
parser.add_argument('--relentless', action="store_true", help="Keep applying forever")
parser.add_argument('--list', action="store_true", help="List all available deployments and exit")
parser.add_argument('--noheadless', action="store_false",help="Show the chromium driver as it fills in the application")
parser.add_argument('--leaveopen', action="store_true", help="Try to leave the browser open after an application is completed")


def main():
    args = parser.parse_args()

    if args.list:
        Deployment.print_deployments()
        sys.exit(0)

    headless = args.noheadless
    deployments = Deployment.get_deployments()
    if args.deployment not in deployments.keys():
        raise ValueError(f"Could not find deployment {args.deployment}, try --list to see which are available")

    deployment = deployments[args.deployment]

    identity_args = {'email_service':args.email}

    if args.relentless:
        while True:
            bot = deployment.make(headless=headless, identity_args=identity_args)
            success = bot.apply()
            bot.quit(args.leaveopen)

    else:
        for i in range(args.n):
            print(colors.GREEN + '-' * 50 + f'\n    applying for job #{i}/{args.n}\n' + '-' * 50 + colors.RESET)
            bot = deployment.make(headless=headless)
            success = bot.apply()
            bot.quit(args.leaveopen)

if __name__ == "__main__":
    main()