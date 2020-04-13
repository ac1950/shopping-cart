
import os
from app.shopping_cart import to_usd, get_tax, get_total_due

def test_to_usd():
    assert to_usd(10.50) == "$10.50"
    assert to_usd(10.58888) == "$10.59"

def test_get_tax():
    assert get_tax(10) == 0.875

def test_get_total_due(): 
    assert get_total_due(10) == "$10.88"


