#!/bin/bash
# Demo: A Day in the Life of a Student Agent
set -e 

echo "--- 1. Teacher Agent Assigns Unit 1.1 (NAND) ---"
echo "$ gap checkpoint verify unit_1_1"
gap checkpoint verify unit_1_1 --root .

echo -e "\n--- 2. Teacher Attempts to Assign Unit 1.2 (Multiplexers) ---"
echo "Policy: Student must review Module 1 before proceeding."
echo "$ gap checkpoint verify unit_1_2"

set +e
gap checkpoint verify unit_1_2 --root .
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -ne 0 ]; then
    echo "✅ ASSIGNMENT BLOCKED (Waiting for Student Readiness)"
else
    echo "❌ FAILED TO BLOCK"
    exit 1
fi

echo -e "\n--- 3. Student Accepts Unit 1.2 ---"
gap checkpoint approve unit_1_2 --root .

echo -e "\n--- 4. Teacher Proceed with Unit 1.2 ---"
gap checkpoint verify unit_1_2 --root .
echo "✅ SUCCESS: Lesson Unlocked"
