# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldinaut <ldinaut@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/22 17:25:57 by ldinaut           #+#    #+#              #
#    Updated: 2024/01/22 18:21:40 by ldinaut          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import date

seconds = time.time()
t = str(seconds).split('.')
form_sec = f"{int(t[0]):,d}"
scientific = "{:.2e}".format(seconds)

today = date.today()
today = today.strftime("%b %d %Y")

print("Seconds since January 1, 1970: ", form_sec, ".",t[1], sep="", end="")
print(" or", scientific, "in scientific notation")
print(today)
