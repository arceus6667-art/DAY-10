{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c107cad-0907-4db3-b61c-00a3f5931253",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Folders created successfully!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "os.makedirs(\"dataset/cats\", exist_ok=True)\n",
    "os.makedirs(\"dataset/dogs\", exist_ok=True)\n",
    "\n",
    "print(\"Folders created successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ebaf2c11-528e-4829-945b-1b9cf8d8e87a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.13.0.92-cp37-abi3-win_amd64.whl.metadata (20 kB)\n",
      "Requirement already satisfied: numpy>=2 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from opencv-python) (2.4.2)\n",
      "Downloading opencv_python-4.13.0.92-cp37-abi3-win_amd64.whl (40.2 MB)\n",
      "   ---------------------------------------- 0.0/40.2 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.3/40.2 MB ? eta -:--:--\n",
      "    --------------------------------------- 0.5/40.2 MB 1.9 MB/s eta 0:00:22\n",
      "    --------------------------------------- 0.8/40.2 MB 1.1 MB/s eta 0:00:37\n",
      "    --------------------------------------- 0.8/40.2 MB 1.1 MB/s eta 0:00:37\n",
      "   - -------------------------------------- 1.0/40.2 MB 915.5 kB/s eta 0:00:43\n",
      "   - -------------------------------------- 1.0/40.2 MB 915.5 kB/s eta 0:00:43\n",
      "   - -------------------------------------- 1.0/40.2 MB 915.5 kB/s eta 0:00:43\n",
      "   - -------------------------------------- 1.0/40.2 MB 915.5 kB/s eta 0:00:43\n",
      "   - -------------------------------------- 1.3/40.2 MB 664.5 kB/s eta 0:00:59\n",
      "   - -------------------------------------- 1.3/40.2 MB 664.5 kB/s eta 0:00:59\n",
      "   - -------------------------------------- 1.6/40.2 MB 590.7 kB/s eta 0:01:06\n",
      "   - -------------------------------------- 1.6/40.2 MB 590.7 kB/s eta 0:01:06\n",
      "   - -------------------------------------- 1.6/40.2 MB 590.7 kB/s eta 0:01:06\n",
      "   - -------------------------------------- 1.8/40.2 MB 592.2 kB/s eta 0:01:05\n",
      "   -- ------------------------------------- 2.4/40.2 MB 688.3 kB/s eta 0:00:55\n",
      "   -- ------------------------------------- 2.6/40.2 MB 725.9 kB/s eta 0:00:52\n",
      "   -- ------------------------------------- 2.6/40.2 MB 725.9 kB/s eta 0:00:52\n",
      "   -- ------------------------------------- 2.9/40.2 MB 717.0 kB/s eta 0:00:53\n",
      "   -- ------------------------------------- 2.9/40.2 MB 717.0 kB/s eta 0:00:53\n",
      "   --- ------------------------------------ 3.1/40.2 MB 726.5 kB/s eta 0:00:52\n",
      "   --- ------------------------------------ 3.4/40.2 MB 721.7 kB/s eta 0:00:51\n",
      "   --- ------------------------------------ 3.9/40.2 MB 804.5 kB/s eta 0:00:46\n",
      "   --- ------------------------------------ 3.9/40.2 MB 804.5 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 4.2/40.2 MB 789.0 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 4.2/40.2 MB 789.0 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 4.5/40.2 MB 791.8 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 4.5/40.2 MB 791.8 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 4.7/40.2 MB 779.2 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 5.0/40.2 MB 772.4 kB/s eta 0:00:46\n",
      "   ---- ----------------------------------- 5.0/40.2 MB 772.4 kB/s eta 0:00:46\n",
      "   ----- ---------------------------------- 5.2/40.2 MB 777.5 kB/s eta 0:00:45\n",
      "   ----- ---------------------------------- 5.2/40.2 MB 777.5 kB/s eta 0:00:45\n",
      "   ----- ---------------------------------- 5.5/40.2 MB 766.1 kB/s eta 0:00:46\n",
      "   ----- ---------------------------------- 5.5/40.2 MB 766.1 kB/s eta 0:00:46\n",
      "   ----- ---------------------------------- 5.8/40.2 MB 756.1 kB/s eta 0:00:46\n",
      "   ----- ---------------------------------- 6.0/40.2 MB 759.4 kB/s eta 0:00:46\n",
      "   ----- ---------------------------------- 6.0/40.2 MB 759.4 kB/s eta 0:00:46\n",
      "   ------ --------------------------------- 6.3/40.2 MB 756.6 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.3/40.2 MB 756.6 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.6/40.2 MB 751.2 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.6/40.2 MB 751.2 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.8/40.2 MB 746.3 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.8/40.2 MB 746.3 kB/s eta 0:00:45\n",
      "   ------ --------------------------------- 6.8/40.2 MB 746.3 kB/s eta 0:00:45\n",
      "   ------- -------------------------------- 7.1/40.2 MB 709.3 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.1/40.2 MB 709.3 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.1/40.2 MB 709.3 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.3/40.2 MB 698.0 kB/s eta 0:00:48\n",
      "   ------- -------------------------------- 7.3/40.2 MB 698.0 kB/s eta 0:00:48\n",
      "   ------- -------------------------------- 7.6/40.2 MB 697.0 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.6/40.2 MB 697.0 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.9/40.2 MB 695.1 kB/s eta 0:00:47\n",
      "   ------- -------------------------------- 7.9/40.2 MB 695.1 kB/s eta 0:00:47\n",
      "   -------- ------------------------------- 8.1/40.2 MB 692.3 kB/s eta 0:00:47\n",
      "   -------- ------------------------------- 8.4/40.2 MB 702.9 kB/s eta 0:00:46\n",
      "   -------- ------------------------------- 8.7/40.2 MB 700.9 kB/s eta 0:00:46\n",
      "   -------- ------------------------------- 8.7/40.2 MB 700.9 kB/s eta 0:00:46\n",
      "   -------- ------------------------------- 8.9/40.2 MB 704.4 kB/s eta 0:00:45\n",
      "   --------- ------------------------------ 9.2/40.2 MB 706.9 kB/s eta 0:00:44\n",
      "   --------- ------------------------------ 9.2/40.2 MB 706.9 kB/s eta 0:00:44\n",
      "   --------- ------------------------------ 9.4/40.2 MB 705.0 kB/s eta 0:00:44\n",
      "   --------- ------------------------------ 9.4/40.2 MB 705.0 kB/s eta 0:00:44\n",
      "   --------- ------------------------------ 9.4/40.2 MB 705.0 kB/s eta 0:00:44\n",
      "   --------- ------------------------------ 9.7/40.2 MB 691.9 kB/s eta 0:00:45\n",
      "   --------- ------------------------------ 9.7/40.2 MB 691.9 kB/s eta 0:00:45\n",
      "   --------- ------------------------------ 9.7/40.2 MB 691.9 kB/s eta 0:00:45\n",
      "   --------- ------------------------------ 9.7/40.2 MB 691.9 kB/s eta 0:00:45\n",
      "   --------- ------------------------------ 10.0/40.2 MB 671.8 kB/s eta 0:00:46\n",
      "   --------- ------------------------------ 10.0/40.2 MB 671.8 kB/s eta 0:00:46\n",
      "   ---------- ----------------------------- 10.2/40.2 MB 667.6 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 10.2/40.2 MB 667.6 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 10.5/40.2 MB 665.6 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 10.5/40.2 MB 665.6 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 10.7/40.2 MB 663.8 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 10.7/40.2 MB 663.8 kB/s eta 0:00:45\n",
      "   ---------- ----------------------------- 11.0/40.2 MB 667.8 kB/s eta 0:00:44\n",
      "   ----------- ---------------------------- 11.3/40.2 MB 670.4 kB/s eta 0:00:44\n",
      "   ----------- ---------------------------- 11.5/40.2 MB 674.2 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 11.5/40.2 MB 674.2 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 11.5/40.2 MB 674.2 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 11.8/40.2 MB 669.3 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 11.8/40.2 MB 669.3 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 12.1/40.2 MB 668.1 kB/s eta 0:00:43\n",
      "   ----------- ---------------------------- 12.1/40.2 MB 668.1 kB/s eta 0:00:43\n",
      "   ------------ --------------------------- 12.3/40.2 MB 664.8 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.3/40.2 MB 664.8 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.6/40.2 MB 663.8 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.6/40.2 MB 663.8 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.6/40.2 MB 663.8 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.8/40.2 MB 656.3 kB/s eta 0:00:42\n",
      "   ------------ --------------------------- 12.8/40.2 MB 656.3 kB/s eta 0:00:42\n",
      "   ------------- -------------------------- 13.4/40.2 MB 663.2 kB/s eta 0:00:41\n",
      "   ------------- -------------------------- 13.6/40.2 MB 673.7 kB/s eta 0:00:40\n",
      "   ------------- -------------------------- 13.9/40.2 MB 675.3 kB/s eta 0:00:39\n",
      "   ------------- -------------------------- 13.9/40.2 MB 675.3 kB/s eta 0:00:39\n",
      "   ------------- -------------------------- 13.9/40.2 MB 675.3 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.2/40.2 MB 671.1 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.2/40.2 MB 671.1 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.4/40.2 MB 670.1 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.4/40.2 MB 670.1 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.7/40.2 MB 666.7 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.7/40.2 MB 666.7 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.7/40.2 MB 666.7 kB/s eta 0:00:39\n",
      "   -------------- ------------------------- 14.9/40.2 MB 662.1 kB/s eta 0:00:39\n",
      "   --------------- ------------------------ 15.2/40.2 MB 664.1 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 15.2/40.2 MB 664.1 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 15.5/40.2 MB 665.1 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 15.5/40.2 MB 665.1 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 15.7/40.2 MB 660.8 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 15.7/40.2 MB 660.8 kB/s eta 0:00:38\n",
      "   --------------- ------------------------ 16.0/40.2 MB 661.0 kB/s eta 0:00:37\n",
      "   --------------- ------------------------ 16.0/40.2 MB 661.0 kB/s eta 0:00:37\n",
      "   ---------------- ----------------------- 16.3/40.2 MB 663.7 kB/s eta 0:00:37\n",
      "   ---------------- ----------------------- 16.3/40.2 MB 663.7 kB/s eta 0:00:37\n",
      "   ---------------- ----------------------- 16.5/40.2 MB 659.6 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.5/40.2 MB 659.6 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.8/40.2 MB 656.9 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.8/40.2 MB 656.9 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.8/40.2 MB 656.9 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.8/40.2 MB 656.9 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 16.8/40.2 MB 656.9 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 17.0/40.2 MB 643.7 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 17.0/40.2 MB 643.7 kB/s eta 0:00:36\n",
      "   ---------------- ----------------------- 17.0/40.2 MB 643.7 kB/s eta 0:00:36\n",
      "   ----------------- ---------------------- 17.3/40.2 MB 635.9 kB/s eta 0:00:37\n",
      "   ----------------- ---------------------- 17.3/40.2 MB 635.9 kB/s eta 0:00:37\n",
      "   ----------------- ---------------------- 17.3/40.2 MB 635.9 kB/s eta 0:00:37\n",
      "   ----------------- ---------------------- 17.6/40.2 MB 631.3 kB/s eta 0:00:36\n",
      "   ----------------- ---------------------- 18.1/40.2 MB 643.1 kB/s eta 0:00:35\n",
      "   ----------------- ---------------------- 18.1/40.2 MB 643.1 kB/s eta 0:00:35\n",
      "   ----------------- ---------------------- 18.1/40.2 MB 643.1 kB/s eta 0:00:35\n",
      "   ------------------ --------------------- 18.4/40.2 MB 641.0 kB/s eta 0:00:35\n",
      "   ------------------ --------------------- 18.4/40.2 MB 641.0 kB/s eta 0:00:35\n",
      "   ------------------ --------------------- 18.6/40.2 MB 638.6 kB/s eta 0:00:34\n",
      "   ------------------- -------------------- 19.1/40.2 MB 652.3 kB/s eta 0:00:33\n",
      "   ------------------- -------------------- 19.1/40.2 MB 652.3 kB/s eta 0:00:33\n",
      "   ------------------- -------------------- 19.1/40.2 MB 652.3 kB/s eta 0:00:33\n",
      "   ------------------- -------------------- 19.4/40.2 MB 649.0 kB/s eta 0:00:33\n",
      "   ------------------- -------------------- 19.4/40.2 MB 649.0 kB/s eta 0:00:33\n",
      "   ------------------- -------------------- 19.7/40.2 MB 647.0 kB/s eta 0:00:32\n",
      "   ------------------- -------------------- 19.7/40.2 MB 647.0 kB/s eta 0:00:32\n",
      "   ------------------- -------------------- 19.7/40.2 MB 647.0 kB/s eta 0:00:32\n",
      "   ------------------- -------------------- 19.9/40.2 MB 634.8 kB/s eta 0:00:32\n",
      "   ------------------- -------------------- 19.9/40.2 MB 634.8 kB/s eta 0:00:32\n",
      "   -------------------- ------------------- 20.2/40.2 MB 639.5 kB/s eta 0:00:32\n",
      "   -------------------- ------------------- 20.4/40.2 MB 642.9 kB/s eta 0:00:31\n",
      "   -------------------- ------------------- 20.4/40.2 MB 642.9 kB/s eta 0:00:31\n",
      "   -------------------- ------------------- 20.7/40.2 MB 646.7 kB/s eta 0:00:31\n",
      "   -------------------- ------------------- 20.7/40.2 MB 646.7 kB/s eta 0:00:31\n",
      "   -------------------- ------------------- 21.0/40.2 MB 647.0 kB/s eta 0:00:30\n",
      "   --------------------- ------------------ 21.2/40.2 MB 650.4 kB/s eta 0:00:30\n",
      "   --------------------- ------------------ 21.5/40.2 MB 657.7 kB/s eta 0:00:29\n",
      "   --------------------- ------------------ 21.8/40.2 MB 658.4 kB/s eta 0:00:29\n",
      "   --------------------- ------------------ 21.8/40.2 MB 658.4 kB/s eta 0:00:29\n",
      "   --------------------- ------------------ 22.0/40.2 MB 648.3 kB/s eta 0:00:29\n",
      "   ---------------------- ----------------- 22.3/40.2 MB 650.7 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 22.3/40.2 MB 650.7 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 22.5/40.2 MB 648.3 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 22.5/40.2 MB 648.3 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 22.8/40.2 MB 639.2 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 22.8/40.2 MB 639.2 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 23.1/40.2 MB 633.1 kB/s eta 0:00:28\n",
      "   ---------------------- ----------------- 23.1/40.2 MB 633.1 kB/s eta 0:00:28\n",
      "   ----------------------- ---------------- 23.3/40.2 MB 632.8 kB/s eta 0:00:27\n",
      "   ----------------------- ---------------- 23.6/40.2 MB 635.1 kB/s eta 0:00:27\n",
      "   ----------------------- ---------------- 23.6/40.2 MB 635.1 kB/s eta 0:00:27\n",
      "   ----------------------- ---------------- 23.6/40.2 MB 635.1 kB/s eta 0:00:27\n",
      "   ----------------------- ---------------- 23.9/40.2 MB 630.4 kB/s eta 0:00:26\n",
      "   ----------------------- ---------------- 23.9/40.2 MB 630.4 kB/s eta 0:00:26\n",
      "   ------------------------ --------------- 24.4/40.2 MB 635.4 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.4/40.2 MB 635.4 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.6/40.2 MB 638.1 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.6/40.2 MB 638.1 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.6/40.2 MB 638.1 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.9/40.2 MB 629.5 kB/s eta 0:00:25\n",
      "   ------------------------ --------------- 24.9/40.2 MB 629.5 kB/s eta 0:00:25\n",
      "   ------------------------- -------------- 25.2/40.2 MB 630.8 kB/s eta 0:00:24\n",
      "   ------------------------- -------------- 25.4/40.2 MB 632.8 kB/s eta 0:00:24\n",
      "   ------------------------- -------------- 25.4/40.2 MB 632.8 kB/s eta 0:00:24\n",
      "   ------------------------- -------------- 25.7/40.2 MB 634.4 kB/s eta 0:00:23\n",
      "   ------------------------- -------------- 26.0/40.2 MB 646.0 kB/s eta 0:00:23\n",
      "   -------------------------- ------------- 26.2/40.2 MB 648.0 kB/s eta 0:00:22\n",
      "   -------------------------- ------------- 26.2/40.2 MB 648.0 kB/s eta 0:00:22\n",
      "   -------------------------- ------------- 26.5/40.2 MB 650.0 kB/s eta 0:00:22\n",
      "   -------------------------- ------------- 26.7/40.2 MB 655.1 kB/s eta 0:00:21\n",
      "   -------------------------- ------------- 26.7/40.2 MB 655.1 kB/s eta 0:00:21\n",
      "   -------------------------- ------------- 27.0/40.2 MB 657.4 kB/s eta 0:00:21\n",
      "   --------------------------- ------------ 27.3/40.2 MB 659.5 kB/s eta 0:00:20\n",
      "   --------------------------- ------------ 27.5/40.2 MB 661.6 kB/s eta 0:00:20\n",
      "   --------------------------- ------------ 27.8/40.2 MB 665.1 kB/s eta 0:00:19\n",
      "   --------------------------- ------------ 27.8/40.2 MB 665.1 kB/s eta 0:00:19\n",
      "   --------------------------- ------------ 28.0/40.2 MB 665.8 kB/s eta 0:00:19\n",
      "   ---------------------------- ----------- 28.3/40.2 MB 665.8 kB/s eta 0:00:18\n",
      "   ---------------------------- ----------- 28.6/40.2 MB 669.7 kB/s eta 0:00:18\n",
      "   ---------------------------- ----------- 28.8/40.2 MB 674.3 kB/s eta 0:00:17\n",
      "   ---------------------------- ----------- 29.1/40.2 MB 678.5 kB/s eta 0:00:17\n",
      "   ----------------------------- ---------- 29.6/40.2 MB 687.6 kB/s eta 0:00:16\n",
      "   ----------------------------- ---------- 29.9/40.2 MB 690.3 kB/s eta 0:00:15\n",
      "   ----------------------------- ---------- 30.1/40.2 MB 697.6 kB/s eta 0:00:15\n",
      "   ------------------------------ --------- 30.4/40.2 MB 700.9 kB/s eta 0:00:14\n",
      "   ------------------------------ --------- 30.9/40.2 MB 716.7 kB/s eta 0:00:13\n",
      "   ------------------------------- -------- 31.2/40.2 MB 721.4 kB/s eta 0:00:13\n",
      "   ------------------------------- -------- 31.5/40.2 MB 726.4 kB/s eta 0:00:13\n",
      "   ------------------------------- -------- 31.7/40.2 MB 739.5 kB/s eta 0:00:12\n",
      "   ------------------------------- -------- 32.0/40.2 MB 743.7 kB/s eta 0:00:12\n",
      "   -------------------------------- ------- 32.2/40.2 MB 749.0 kB/s eta 0:00:11\n",
      "   -------------------------------- ------- 32.8/40.2 MB 760.2 kB/s eta 0:00:10\n",
      "   -------------------------------- ------- 32.8/40.2 MB 760.2 kB/s eta 0:00:10\n",
      "   -------------------------------- ------- 33.0/40.2 MB 763.4 kB/s eta 0:00:10\n",
      "   -------------------------------- ------- 33.0/40.2 MB 763.4 kB/s eta 0:00:10\n",
      "   --------------------------------- ------ 33.3/40.2 MB 762.2 kB/s eta 0:00:10\n",
      "   --------------------------------- ------ 33.3/40.2 MB 762.2 kB/s eta 0:00:10\n",
      "   --------------------------------- ------ 33.3/40.2 MB 762.2 kB/s eta 0:00:10\n",
      "   --------------------------------- ------ 33.6/40.2 MB 755.4 kB/s eta 0:00:09\n",
      "   --------------------------------- ------ 33.6/40.2 MB 755.4 kB/s eta 0:00:09\n",
      "   --------------------------------- ------ 33.6/40.2 MB 755.4 kB/s eta 0:00:09\n",
      "   --------------------------------- ------ 33.8/40.2 MB 745.1 kB/s eta 0:00:09\n",
      "   --------------------------------- ------ 33.8/40.2 MB 745.1 kB/s eta 0:00:09\n",
      "   --------------------------------- ------ 34.1/40.2 MB 750.5 kB/s eta 0:00:09\n",
      "   ---------------------------------- ----- 34.3/40.2 MB 753.0 kB/s eta 0:00:08\n",
      "   ---------------------------------- ----- 34.6/40.2 MB 758.6 kB/s eta 0:00:08\n",
      "   ---------------------------------- ----- 34.9/40.2 MB 763.4 kB/s eta 0:00:08\n",
      "   ---------------------------------- ----- 35.1/40.2 MB 767.0 kB/s eta 0:00:07\n",
      "   ----------------------------------- ---- 35.4/40.2 MB 770.6 kB/s eta 0:00:07\n",
      "   ----------------------------------- ---- 35.7/40.2 MB 774.2 kB/s eta 0:00:06\n",
      "   ----------------------------------- ---- 35.9/40.2 MB 783.7 kB/s eta 0:00:06\n",
      "   ----------------------------------- ---- 35.9/40.2 MB 783.7 kB/s eta 0:00:06\n",
      "   ----------------------------------- ---- 36.2/40.2 MB 783.8 kB/s eta 0:00:06\n",
      "   ----------------------------------- ---- 36.2/40.2 MB 783.8 kB/s eta 0:00:06\n",
      "   ------------------------------------ --- 36.4/40.2 MB 787.1 kB/s eta 0:00:05\n",
      "   ------------------------------------ --- 36.4/40.2 MB 787.1 kB/s eta 0:00:05\n",
      "   ------------------------------------ --- 36.7/40.2 MB 769.8 kB/s eta 0:00:05\n",
      "   ------------------------------------ --- 37.0/40.2 MB 770.2 kB/s eta 0:00:05\n",
      "   ------------------------------------ --- 37.0/40.2 MB 770.2 kB/s eta 0:00:05\n",
      "   ------------------------------------- -- 37.2/40.2 MB 776.2 kB/s eta 0:00:04\n",
      "   ------------------------------------- -- 37.5/40.2 MB 778.7 kB/s eta 0:00:04\n",
      "   ------------------------------------- -- 37.7/40.2 MB 779.7 kB/s eta 0:00:04\n",
      "   ------------------------------------- -- 37.7/40.2 MB 779.7 kB/s eta 0:00:04\n",
      "   ------------------------------------- -- 38.0/40.2 MB 784.2 kB/s eta 0:00:03\n",
      "   -------------------------------------- - 38.3/40.2 MB 788.5 kB/s eta 0:00:03\n",
      "   -------------------------------------- - 38.5/40.2 MB 796.8 kB/s eta 0:00:03\n",
      "   -------------------------------------- - 38.8/40.2 MB 800.6 kB/s eta 0:00:02\n",
      "   -------------------------------------- - 39.1/40.2 MB 803.9 kB/s eta 0:00:02\n",
      "   ---------------------------------------  39.6/40.2 MB 813.1 kB/s eta 0:00:01\n",
      "   ---------------------------------------  39.8/40.2 MB 816.5 kB/s eta 0:00:01\n",
      "   ---------------------------------------  40.1/40.2 MB 825.6 kB/s eta 0:00:01\n",
      "   ---------------------------------------  40.1/40.2 MB 825.6 kB/s eta 0:00:01\n",
      "   ---------------------------------------- 40.2/40.2 MB 820.0 kB/s eta 0:00:00\n",
      "Installing collected packages: opencv-python\n",
      "Successfully installed opencv-python-4.13.0.92\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.1.1 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install opencv-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fc69b7d9-facf-41dd-902d-8a415cf728a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: opencv-python in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (4.13.0.92)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (1.8.0)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (3.10.8)\n",
      "Requirement already satisfied: seaborn in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (0.13.2)\n",
      "Requirement already satisfied: joblib in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (1.5.3)\n",
      "Requirement already satisfied: numpy>=2 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from opencv-python) (2.4.2)\n",
      "Requirement already satisfied: scipy>=1.10.0 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from scikit-learn) (1.17.1)\n",
      "Requirement already satisfied: threadpoolctl>=3.2.0 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from scikit-learn) (3.6.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (1.3.3)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (4.61.1)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (1.4.9)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (26.0)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (12.1.1)\n",
      "Requirement already satisfied: pyparsing>=3 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (3.3.2)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: pandas>=1.2 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from seaborn) (2.3.3)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from pandas>=1.2->seaborn) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from pandas>=1.2->seaborn) (2025.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\parth\\pycharmprojects\\pythonproject3\\.venv\\lib\\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.1.1 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install opencv-python scikit-learn matplotlib seaborn joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75807e67-7a8e-466e-ae71-03afb23a25ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import cv2\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import classification_report, confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "67008fea-fdf3-4184-b3f5-73f653228584",
   "metadata": {},
   "outputs": [],
   "source": [
    "DATADIR = 'dataset'\n",
    "# Change these to match your actual folder names if you rename them\n",
    "CATEGORIES = ['cats', 'dogs'] \n",
    "IMG_SIZE = 100 # Resizing to 100x100 for consistency\n",
    "\n",
    "X = []\n",
    "y = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dab0ccf7-5adf-4b9f-a013-c7ecebfe204e",
   "metadata": {},
   "outputs": [],
   "source": [
    "for category in CATEGORIES:\n",
    "    path = os.path.join(DATADIR, category)\n",
    "    class_num = CATEGORIES.index(category)\n",
    "    \n",
    "    if not os.path.exists(path):\n",
    "        print(f\"Warning: Folder {path} not found.\")\n",
    "        continue\n",
    "\n",
    "    for img in os.listdir(path):\n",
    "        try:\n",
    "            img_path = os.path.join(path, img)\n",
    "            # Read in grayscale to simplify the SVM processing\n",
    "            img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) \n",
    "            if img_array is not None:\n",
    "                resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))\n",
    "                X.append(resized_array.flatten()) # Flatten the 2D image into a 1D array\n",
    "                y.append(class_num)\n",
    "        except Exception as e:\n",
    "            pass # Skip broken or unreadable images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f0489f50-774f-4dce-9cce-e1135f27758a",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = np.array(X)\n",
    "y = np.array(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "15f64c36-c8d3-40f5-8d60-e909e18b8a31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total images loaded: 5516\n"
     ]
    }
   ],
   "source": [
    "print(f\"Total images loaded: {len(X)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a9b888a3-14a5-4387-bcbf-1691a61a05fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = X / 255.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c7956000-4745-43c9-baa3-574ad40b8292",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2f4b8ed4-215c-4497-838a-2810135210e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training SVM model. This might take a minute depending on your dataset size...\n",
      "Training complete!\n"
     ]
    }
   ],
   "source": [
    "print(\"Training SVM model. This might take a minute depending on your dataset size...\")\n",
    "model = SVC(kernel='linear', probability=True, random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "print(\"Training complete!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "08a66e49-a024-4677-8564-f72ac475017e",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "142cf44d-fe6c-45d4-a88e-43e3d13e859c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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h0APAAC6pegg0iPrHgAAQMNQogcAAN1StF+glzoL1doHAQAAAAkDVfcAAAAahkAPAACgYQj0AAAAGoZADwAAoGEI9AAAABqGQA8AAKBhCPQAAAAahkAPAACgYQj0AAAAGoZAD59c7969cVbB5owZM4b2799v7cMA+OQQ6OGT8vT0pF9//RVnFQAgiUCgh09K0cMdIgAAbAgCPbyTi4sLbd++nV68eEG3b9+mb7/9VuY3aNCAzpw5Qy9fvqSnT5/SihUrKE2aNJQvXz7y9vaWdVRVpWrVqlGePHlo586d8hoPHjyg2bNnk709bpoI1ufm5kaHDh2isLAw2rt3L2XNmtW4rEKFCrIsNDSUbty4QT179jTbdsCAARQYGEjPnz+nWbNm0b59+6hjx46yrHr16nT27Fn5+7h+/Tr16NEj0d8bQHR89zpMOAdm34EUKVKo169fV9euXau6u7ur9evXV1+8eKH269dPjYyMVLt166bmy5dPrV27thocHKwOHDhQtbOzU5s0aaIyR0dHNXny5OqmTZvU9evXqy4uLmrFihXVu3fvqr1798b3Dd83q34HHBwc1Bs3bqhLly5VixQpIt/JV69eqfv371ddXV3V8PBwdeLEiWrhwoXVDh06qKGhoWrjxo1l2zZt2qjPnz9XmzdvLn8bmzdvVt++fat27NhR/gYePXqkjhgxQv4+eN03b96obm5u+M7jO69a8RwgyOMcxPwONGjQQA0JCVHTpk1rnNepUye1b9++ao8ePczWXbFihbpw4UJ5XK1aNQn0hmW+vr6ql5eXam9vL89LliwpP4A45/i7s+Z3oF69ehKsU6dObZy3evVqCfTTp09Xjxw5Yrb+pEmT1KNHj8pjXjZu3DjjsowZM8qFAAf6TJkyyfe/a9euxuWff/65rIPvPL7zZKVzgKp7iFWRIkXo6tWrUnVpsGTJEpo7d65U548YMUKq7M+dO0ctWrSgZMmSxfo6U6ZMobZt29LDhw9lfa7e52YAAGtyd3ena9euUXh4uHGej4+PsUr/xIkTZusfPXpU5rMSJUoY12XPnj2jK1euyGNuyuJk1IULF9KtW7dozpw5Ur3P6wBYCwI9xOr169exzucfuYsXL8oP5cGDB6lr1660atWqd55FDu558+alYcOGUbp06WjdunU0fvx4nHVIcomjr169kv8jIiJirMsXsoaL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",
      "text/plain": [
       "<Figure size 600x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(6,4))\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=CATEGORIES, yticklabels=CATEGORIES)\n",
    "plt.title('SVM Classification Confusion Matrix')\n",
    "plt.ylabel('Actual')\n",
    "plt.xlabel('Predicted')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b26039c0-d2a5-4f97-9bb2-e109404cd583",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "        cats       0.59      0.61      0.60       656\n",
      "        dogs       0.41      0.39      0.40       448\n",
      "\n",
      "    accuracy                           0.52      1104\n",
      "   macro avg       0.50      0.50      0.50      1104\n",
      "weighted avg       0.52      0.52      0.52      1104\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nClassification Report:\\n\", classification_report(y_test, y_pred, target_names=CATEGORIES))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e3d72f7d-2369-4052-b2a4-c17abed9eee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fadd8192-0605-4e9b-9d0a-4cdc194d6a89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model saved successfully as 'svm_face_model.pkl' for Streamlit deployment.\n"
     ]
    }
   ],
   "source": [
    "joblib.dump(model, 'svm_face_model.pkl')\n",
    "print(\"Model saved successfully as 'svm_face_model.pkl' for Streamlit deployment.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b17aeda9-f89d-48cf-a435-9e8169731fde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extracting features with PCA and training RBF SVM...\n"
     ]
    }
   ],
   "source": [
    "from sklearn.svm import SVC\n",
    "from sklearn.decomposition import PCA\n",
    "from sklearn.pipeline import make_pipeline\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "# --- The \"Too Much Accurate\" Pipeline ---\n",
    "print(\"Extracting features with PCA and training RBF SVM...\")\n",
    "# 1. PCA extracts the top 150 most important visual patterns\n",
    "pca = PCA(n_components=150, whiten=True, random_state=42)\n",
    "# 2. RBF Kernel SVM handles the complex, non-linear classification\n",
    "svc = SVC(kernel='rbf', C=10, gamma='scale', probability=True, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bf70c1fd-25f8-449c-b1f5-7fc1e25dcaa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. PCA extracts the top 150 most important visual patterns\n",
    "pca = PCA(n_components=150, whiten=True, random_state=42)\n",
    "# 2. RBF Kernel SVM handles the complex, non-linear classification\n",
    "svc = SVC(kernel='rbf', C=10, gamma='scale', probability=True, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0bb921e0-3877-4b23-a96b-b256de1ca32c",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = make_pipeline(pca, svc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "91879f30-0d7f-494f-806b-eea240dcf483",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training complete!\n"
     ]
    }
   ],
   "source": [
    "model.fit(X_train, y_train)\n",
    "print(\"Training complete!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fb71d200-c21b-4d4c-a61b-4ef180ed9495",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ae95f247-ff2d-470c-885d-255ce7e2ab54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 600x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(6,4))\n",
    "cm = confusion_matrix(y_test, y_pred)\n",
    "sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=CATEGORIES, yticklabels=CATEGORIES)\n",
    "plt.title('Advanced SVM (PCA + RBF) Confusion Matrix')\n",
    "plt.ylabel('Actual')\n",
    "plt.xlabel('Predicted')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "af30c97a-cbfc-4404-8676-ec15dd7d1f8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "        cats       0.67      0.74      0.70       656\n",
      "        dogs       0.55      0.47      0.51       448\n",
      "\n",
      "    accuracy                           0.63      1104\n",
      "   macro avg       0.61      0.61      0.61      1104\n",
      "weighted avg       0.62      0.63      0.63      1104\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nClassification Report:\\n\", classification_report(y_test, y_pred, target_names=CATEGORIES))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2b630a16-0992-467f-9995-b6ccc521b3a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model saved successfully as 'svm_advanced_model.pkl'.\n"
     ]
    }
   ],
   "source": [
    "joblib.dump(model, 'svm_advanced_model.pkl')\n",
    "print(\"Model saved successfully as 'svm_advanced_model.pkl'.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6672f58d-a385-4bd5-b6d2-ce244a129dc3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
