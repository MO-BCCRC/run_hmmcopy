library(HMMcopy)

args <- commandArgs(TRUE)

tumour_copy <- args[1]
tumour_table <- args[2]
normal_copy <- args[3]
normal_table <- args[4]
segments <- args[5]
obj_file <- args[6]
sample_id <- args[7]
normal_table_out <- args[8]
tumour_table_out <- args[9]


load(tumour_copy)
tumour_copy <- infile_copy
remove(infile_copy)

tumour_table <- read.table(tumour_table, as.is=T, header=T, check.names=FALSE)

if (normal_copy != 'NULL')
{
    load(normal_copy)
    normal_copy <- infile_copy
    #if normal copy is not null then normalize the tumour by normal
    tumour_copy$copy <- tumour_copy$copy - normal_copy$copy

    normal_table <- read.table(normal_table, as.is=T, header=T, check.names=FALSE)
}

# call copy numbers using default parameters
tumour_segments <- HMMsegment(tumour_copy)


save(tumour_segments, file=paste(obj_file))

segs <- tumour_segments$segs
segs <- cbind(sample_id=sample_id,segs)
write.table(segs, file = segments, col.names = TRUE, row.names = FALSE, quote = FALSE, sep ="\t")

tumour_table$state <- tumour_segments$state
write.table(tumour_table, file = tumour_table_out, col.names = TRUE, row.names = FALSE, quote = FALSE, sep ="\t")

if (normal_copy != 'NULL')
{
	normal_table$state <- tumour_segments$state
	write.table(normal_table, file = normal_table_out, col.names = TRUE, row.names = FALSE, quote = FALSE, sep ="\t")
}



