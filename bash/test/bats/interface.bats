#!/usr/bin/env bats

yf=../../dist/yf
@test "Compiled source" {
  [ -f "$yf" ]
}

@test "Proper action headers" {  
  headers=$(./$yf actions -t MSFT | head -n1)
  result="Date,Dividends,Stock Splits"

  [ "$headers" = "$result" ]
}

@test "Proper calendar row labels" {
  labels=$(./$yf calendar -t MSFT | awk -F ',' '{ print $1 }' | xargs)
  result="Earnings Date Earnings Average Earnings Low Earnings High Revenue Average Revenue Low Revenue High"

  [ "$labels" = "$result" ]
}

@test "Proper dividends headers" {
  headers=$(./$yf dividends -t MSFT | head -n1)
  result="Date,Dividends"

  [ "$headers" = "$result" ]
}

@test "Proper history headers" {
  headers=$(./$yf history -t MSFT | head -n1)
  result="Date,Open,High,Low,Close,Volume,Dividends,Stock Splits"
  
  [ "$headers" = "$result" ]
}

@test "Proper holders headers" {
  headers=$(./$yf holders -t MSFT | head -n1)
  result=",Holder,Shares,Date Reported,% Out,Value"

  [ "$headers" = "$result" ]
}

@test "Proper sustainability headers" {
  headers=$(./$yf sustain -t MSFT | head -n1)

  isProperHeaders=0
  if [[ $headers =~ ^[0-9]{4}-[0-9]{1,2}(,Value) ]]
    then isProperHeaders=1
  fi

  [ "$isProperHeaders" = "1" ]
}
