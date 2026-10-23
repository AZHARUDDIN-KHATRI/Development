#!/bin/bash

git add .
git commit -m "Updated project"
git push origin main

echo "GitHub push completed!"
Save it as push.sh in your project folder and run:

bash
chmod +x push.sh
./push.sh