print('--- DRAFT PHASE COMPLETE ---')
draft = 'Delete all files in /tmp'
print(f'Plan: {draft}')
choice = input('Review Plan. Proceed? (y/n): ')
if choice.lower() == 'y':
    print('PROCEED: Executing plan...')
else:
    print('HALT: Agent suspended.')
