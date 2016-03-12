#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='.', url='postgresql://pto_tracker:26fbb64a0c95fa83b69585c11610543e@localhost:5432/pto_tracker', debug='False')
