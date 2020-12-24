#!/usr/bin/env bats

YF_PATH=dist/yf
@test "Compiled source" {
  [ -f $YF_PATH ]
}

@test "Proper action headers" {  
  headers=$(./$YF_PATH actions -t MSFT | head -n1)
  result="Date,Dividends,Stock Splits"

  [ "$headers" = "$result" ]
}

@test "Proper calendar row labels" {
  labels=$(./$YF_PATH calendar -t MSFT | awk -F ',' '{ print $1 }' | xargs)
  result="Earnings Date Earnings Average Earnings Low Earnings High Revenue Average Revenue Low Revenue High"

  [ "$labels" = "$result" ]
}

@test "Proper dividends headers" {
  headers=$(./$YF_PATH dividends -t MSFT | head -n1)
  result="Date,Dividends"

  [ "$headers" = "$result" ]
}

@test "Proper history headers" {
  headers=$(./$YF_PATH history -t MSFT | head -n1)
  result="Date,Open,High,Low,Close,Volume,Dividends,Stock Splits"
  
  [ "$headers" = "$result" ]
}

@test "Proper holders headers" {
  headers=$(./$YF_PATH holders -t MSFT | head -n1)
  result=",Holder,Shares,Date Reported,% Out,Value"

  [ "$headers" = "$result" ]
}

@test "Proper sustainability headers" {
  headers=$(./$YF_PATH sustain -t MSFT | head -n1)

  isProperHeaders=0
  if [[ $headers =~ ^[0-9]{4}-[0-9]{1,2}(,Value) ]]
    then isProperHeaders=1
  fi

  [ "$isProperHeaders" = "1" ]
}
