#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<match>(?<=from:|to:|flags:).+?(?=\]))/).join(',')
