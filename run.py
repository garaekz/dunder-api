#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import server
from dotenv import load_dotenv
load_dotenv() 

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    server.run('0.0.0.0', port=port)
