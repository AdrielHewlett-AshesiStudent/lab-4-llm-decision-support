SUMMARY_PROMPT=['Summarize this letter:\n'
 'Hi,\n'
 'This is Kofi. I saw your advert. I want GHS 50,000 to start a car washing '
 'business, a\n'
 'provision shop, and also import phones from Dubai. I am 22 and full of '
 'energy. I have not\n'
 'started any of these yet but my friends say I am very business minded. I '
 'will pay back in\n'
 'one year when the businesses are booming. No collateral but I am '
 'trustworthy.\n',
 ["You are a microfinance loan officer's assistant. Be neutral, pragmatic yet "
  'considerate. Be professional and resourceful.',
  'Summarize this letter:\n'
  'Hi,\n'
  'This is Kofi. I saw your advert. I want GHS 50,000 to start a car washing '
  'business, a\n'
  'provision shop, and also import phones from Dubai. I am 22 and full of '
  'energy. I have not\n'
  'started any of these yet but my friends say I am very business minded. I '
  'will pay back in\n'
  'one year when the businesses are booming. No collateral but I am '
  'trustworthy.\n',
  'Kwame Boateng, a commercial driver from Kumasi, is requesting a loan of GHS '
  "25,000 to repair his vehicle's engine and settle personal debts. He "
  'mentions that business is currently slow due to the festive season, but '
  'expects it to improve afterwards. He is unable to provide collateral at '
  'this time and is asking for a quick decision on his loan application, '
  'assuring repayment when his financial situation improves.']]
EXTRACT_PROMPT=['Return only a JSON object with applicant_name (string), amount_ghs (number), '
 'purpose (string), \n'
 'monthly_profit_ghs (number or null), has_collateral_or_guarantor (boolean), '
 'repayment_months (number or null).']
BRIEF_PROMPT=[]#My token limit for the API has finished so I have to wait till tomorrow to rerun cells and get this variable
