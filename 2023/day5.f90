program day5
    !$ Brute force resolution of AoC day5
    !$ Note: execution should take around 8 minutes
    !$ * Requires <gfortran> compiler
    !$ * Can be compiled by running:
    !$ > gfortran -O3 -o exec day5.f90
    !$ * Can be executed by running:
    !$ > ./exec
    implicit none
    character (LEN=30) :: string, file_name
    integer :: i, n_seeds, file_id = 10, len_file = 0
    integer(kind=8) ::  min_loc, destination, source, kk
    integer :: line_sts, line_stf, line_ftw, line_wtl, line_ltt, line_tth, line_htl
    integer(kind=8), dimension(:, :), allocatable :: sts_map, stf_map, ftw_map, wtl_map, ltt_map, tth_map, htl_map
    integer(kind=8), dimension(:), allocatable :: seeds
    real(kind=8) :: t1, t2
    
    call cpu_time(t1)
    
    file_name = "input5"
    
    n_seeds = 20
    len_file = 245
    line_sts = 3
    line_stf = 48
    line_ftw = 63
    line_wtl = 110
    line_ltt = 147
    line_tth = 162
    line_htl = 198
    
    allocate(seeds(n_seeds))
    allocate(sts_map(1:3, 1:line_stf - line_sts - 2))
    allocate(stf_map(1:3, 1:line_ftw - line_stf - 2))
    allocate(ftw_map(1:3, 1:line_wtl - line_ftw - 2))
    allocate(wtl_map(1:3, 1:line_ltt - line_wtl - 2))
    allocate(ltt_map(1:3, 1:line_tth - line_ltt - 2))
    allocate(tth_map(1:3, 1:line_htl - line_tth - 2))
    allocate(htl_map(1:3, 1:len_file - line_htl))
    
    open(file_id, file=file_name, form="formatted")
    do i = 1, len_file
        if (i == 1) then
            read(file_id, *) string, seeds(1:n_seeds)
        elseif (i > line_sts .and. i < line_stf - 1) then
            read(file_id, *) sts_map(1:3, i - line_sts)
        elseif (i > line_stf .and. i < line_ftw - 1) then
            read(file_id, *) stf_map(1:3, i - line_stf)
        elseif (i > line_ftw .and. i < line_wtl - 1) then
            read(file_id, *) ftw_map(1:3, i - line_ftw)
        elseif (i > line_wtl .and. i < line_ltt - 1) then
            read(file_id, *) wtl_map(1:3, i - line_wtl)
        elseif (i > line_ltt .and. i < line_tth - 1) then
            read(file_id, *) ltt_map(1:3, i - line_ltt)
        elseif (i > line_tth .and. i < line_htl - 1) then
            read(file_id, *) tth_map(1:3, i - line_tth)
        elseif (i > line_htl .and. i <= len_file) then
            read(file_id, *) htl_map(1:3, i - line_htl)
        else
            read(file_id, *)
        end if
    end do
    close(file_id)
    
    do i = 1, n_seeds
        source = seeds(i)
        destination = source_to_dest(source, size(sts_map, 2), sts_map)
        destination = source_to_dest(destination, size(stf_map, 2), stf_map)
        destination = source_to_dest(destination, size(ftw_map, 2), ftw_map)
        destination = source_to_dest(destination, size(wtl_map, 2), wtl_map)
        destination = source_to_dest(destination, size(ltt_map, 2), ltt_map)
        destination = source_to_dest(destination, size(tth_map, 2), tth_map)
        destination = source_to_dest(destination, size(htl_map, 2), htl_map)
        if (i == 1) then
            min_loc = destination
        else if (destination < min_loc) then
            min_loc = destination
        end if
    end do
    
    call cpu_time(t2)
    write(*, "(a, I10, a, f8.3, a)") "Question 1: the lowest location =", min_loc, &
        & " in ", t2 - t1, " sec."
    
    do i = 1, n_seeds, 2
        do kk = seeds(i), seeds(i) + seeds(i + 1)
            destination = source_to_dest(kk, size(sts_map, 2), sts_map)
            destination = source_to_dest(destination, size(stf_map, 2), stf_map)
            destination = source_to_dest(destination, size(ftw_map, 2), ftw_map)
            destination = source_to_dest(destination, size(wtl_map, 2), wtl_map)
            destination = source_to_dest(destination, size(ltt_map, 2), ltt_map)
            destination = source_to_dest(destination, size(tth_map, 2), tth_map)
            destination = source_to_dest(destination, size(htl_map, 2), htl_map)
            if (i == 1 .and. kk == seeds(1)) then
                min_loc = destination 
            else if (destination < min_loc) then
                min_loc = destination
            end if
        end do
        call cpu_time(t2)
        write(*, "(I2, a, I2, a, I2, a, I10, a, f8.3, a)") i, " -> ", i + 1, "/", n_seeds, &
            & " >> min = ", min_loc, " in ", t2 - t1, " sec."
    end do
    
    write(*, "(a, I10, a, f8.3, a)") "Question 2: the lowest location =", min_loc, &
        & " in ", t2 - t1, " sec."

    deallocate(seeds)
    deallocate(sts_map)
    deallocate(stf_map)
    deallocate(ftw_map)
    deallocate(wtl_map)
    deallocate(ltt_map)
    deallocate(tth_map)
    deallocate(htl_map)
    
    contains
        integer(kind=8) function source_to_dest(source, size_map, map)
            implicit none
            integer(kind=8), intent(in) :: source
            integer, intent(in) :: size_map
            integer(kind=8), dimension(1:3, 1:size_map), intent(in) :: map
            integer :: ii
            source_to_dest = source
            do ii = 1, size_map
                if (source >= map(2, ii) .and. source < map(2, ii) + map(3, ii)) then
                    source_to_dest = map(1, ii) + (source - map(2, ii))
                    exit
                end if
            end do
        end function source_to_dest
    
    end program day5