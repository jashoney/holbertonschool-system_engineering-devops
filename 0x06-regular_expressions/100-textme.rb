#!/usr/bin/env ruby
#this is a comment

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\] /).join(',')
